from datetime import datetime, timedelta
import humanize
import logging
from odoo import models, fields, api, _
from odoo import sql_db
import requests
from urlparse import urljoin

_logger = logging.getLogger(__name__)

ASTERISK_ROLE = 'asterisk' # This PostgreSQL role is used to grant access to CDR table

DISPOSITION_TYPES = (
    ('NO ANSWER', 'No answer'),
    ('FAILED', 'Failed'),
    ('BUSY', 'Busy'),
    ('ANSWERED', 'Answered'),
    ('CONGESTION', 'Congestion'),
)


class Cdr(models.Model):
    _name = 'asterisk.cdr'
    _description = 'Call Detail Record'
    _order = 'started desc'
    _rec_name = 'uniqueid'

    accountcode = fields.Char(size=20, string='Account code', index=True)
    src = fields.Char(size=80, string='Src', index=True)
    dst = fields.Char(size=80, string='Dst', index=True)
    dcontext = fields.Char(size=80, string='Dcontext')
    clid = fields.Char(size=80, string='Clid', index=True)
    channel = fields.Char(size=80, string='Channel', index=True)
    dstchannel = fields.Char(size=80, string='Dst channel', index=True)
    lastapp = fields.Char(size=80, string='Last app')
    lastdata = fields.Char(size=80, string='Last data')
    started = fields.Datetime(index=True, oldname='start')
    answered = fields.Datetime(index=True, oldname='answer')
    ended = fields.Datetime(index=True, oldname='end')
    duration = fields.Integer(string='Duration', index=True)
    billsec = fields.Integer(string='Billsec', index=True)
    disposition = fields.Char(size=45, string='Disposition', index=True)
    amaflags = fields.Integer(string='AMA flags')
    userfield = fields.Char(size=255, string='Userfield')
    uniqueid = fields.Char(size=150, string='Uniqueid', index=True)
    peeraccount = fields.Char(size=20, string='Peer account', index=True)
    linkedid = fields.Char(size=150, string='Linked id')
    sequence = fields.Integer(string='Sequence')
    recording_filename = fields.Char()
    recording_data = fields.Binary()
    recording_widget = fields.Char(compute='_get_recording_widget')
    # QoS
    ssrc = fields.Char(string='Our SSRC')
    themssrc = fields.Char(string='Other SSRC')
    lp = fields.Integer(string='Local Lost Packets')
    rlp = fields.Integer(string='Remote Lost Packets')
    rxjitter = fields.Float(string='RX Jitter')
    txjitter = fields.Float(string='TX Jitter')
    rxcount = fields.Integer(string='RX Count')
    txcount = fields.Integer(string='TX Count')
    rtt = fields.Float(string='Round Trip Time')
    # CEL related fields
    cel_count = fields.Integer(compute='_get_cel_count')
    cels = fields.One2many(comodel_name='asterisk.cel',
                           inverse_name='cdr')

    from_partner = fields.Many2one('res.partner', compute='_get_from_partner', readonly=True)
    to_partner = fields.Many2one('res.partner', compute='_get_to_partner', readonly=True)
    # from_partner_id = fields.Integer(compute='_get_from_partner_id', readonly=True, store=True)
    from_partner_id = fields.Integer(store=True)
    # to_partner_id = fields.Integer(compute='_get_to_partner_id', readonly=True, store=True)
    to_partner_id = fields.Integer(store=True)

    @api.model
    def create(self, values):
        _logger.info("Create cdr")
        new_id = super(Cdr, self).create(vals=values)
        _logger.info(values)
        return new_id

    @api.one
    @api.depends('src')
    def _get_from_partner(self):
        src_internal = False
        if len(self.src) <= 3:
            src_internal = True
        user_src = self.env['res.users'].search([('sip_peer.callerid', '=', self.src,)], limit=1)
        self.from_partner = user_src.partner_id if user_src and src_internal else self.env['res.partner'].sudo().search(['|', ('phone', 'like', self.src,), ('mobile', 'like', self.src,)],
                                                             limit=1).id

    # @api.one
    @api.onchange('src')
    def _get_from_partner_id(self):
        _logger.info("!!!!!!!!!!!!!!!!!!!!!!! _get_from_partner_id")
        self.from_partner_id = self.from_partner.id


    @api.one
    @api.depends('src','dst')
    def _get_to_partner(self):
        dst_internal = False
        if len(self.src) <= 3:
            dst = self.dst
            if len(dst) > 3:
                dst = dst[-10:]
            else:
                dst_internal = True
        else:
            dst = self.dstchannel.split('/')[1].split('-')[0]
        user_dst = self.env['res.users'].search([('sip_peer.callerid', '=', dst,)], limit=1)
        self.to_partner = user_dst.partner_id if user_dst and dst_internal else self.env['res.partner'].search(['|', ('phone', 'like', dst,), ('mobile', 'like', dst,)],
                                                                                                           limit=1)
    # @api.one
    @api.onchange('dst')
    def _get_to_partner_id(self):
        _logger.info("!!!!!!!!!!!!!!!!!!!!!!! _get_to_partner_id")
        self.to_partner_id = self.to_partner.id

    @api.multi
    def _get_cel_count(self):
        for rec in self:
            rec.cel_count = self.env['asterisk.cel'].search_count([
                ('cdr', '=', rec.id)])


    @api.model
    def grant_asterisk_access(self):
        cr = sql_db.db_connect(self.env.cr.dbname).cursor()
        sql = "GRANT ALL on asterisk_cdr to %s" % ASTERISK_ROLE
        cr.execute(sql)
        sql = "GRANT ALL on asterisk_cdr_id_seq to %s" % ASTERISK_ROLE
        cr.execute(sql)
        cr.commit()
        cr.close()


    @api.multi
    def _get_recording_widget(self):
        for rec in self:
            rec.recording_widget = '<audio id="sound_file" preload="auto" ' \
                    'controls="controls"> ' \
                    '<source src="/web/content?model=asterisk.cdr&' \
                    'id={}&filename={}.wav&field=recording_data" ' \
                    'type="audio/wav"/>'.format(rec.id, rec.recording_filename)


    @api.model
    def update_qos(self, values):
        _logger.debug(values)
        uniqueid = values.get('uniqueid')
        linkedid = values.get('linkedid')
        # TODO Probably we need to optimize db query on millions of records.
        cdrs = self.env['asterisk.cdr'].search([
            #('ended', '>', (datetime.now() - timedelta(seconds=120)).strftime(
            #    '%Y-%m-%d %H:%M:%S')
            #),
            ('uniqueid', '=', uniqueid),
            #('linkedid', '=', linkedid),
        ])
        if not cdrs:
            _logger.warning('Omitting QoS, CDR not found, uniqueid {}!'.format(
                uniqueid))
            return False
        else:
            _logger.debug('Found CDR for QoS.')
            cdr = cdrs[0]
            cdr.ssrc =values.get('ssrc')
            cdr.themssrc = values.get('themssrc')
            cdr.lp = int(values.get('lp'))
            cdr.rlp = int(values.get('rlp'))
            cdr.rxjitter = float(values.get('rxjitter'))
            cdr.txjitter = float(values.get('txjitter'))
            cdr.rxcount = int(values.get('rxcount'))
            cdr.txcount = int(values.get('txcount'))
            cdr.rtt = float(values.get('rtt'))
            return True


    @api.model
    def save_call_recording(self, call_id, file_data):
        _logger.info('save_call_recording for callid.')
        rec = self.env['asterisk.cdr'].search([('uniqueid', '=', call_id),], limit=1, order='id desc')
        _logger.info('Rec ID: %s' % rec.id)
        _logger.info('Rec FROM: %s' % rec.from_partner.id)
        _logger.info('Rec To: %s' % rec.to_partner.id)
        rec.from_partner_id = rec.from_partner.id
        rec.to_partner_id = rec.to_partner.id

        if not rec:
            _logger.warning('save_call_recording - cdr not found by id {}.'.format(call_id))
            return False
        else:
            rec.recording_filename = '{}.wav'.format(call_id)
            rec.recording_data = file_data
            return True

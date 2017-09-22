# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    call_count = fields.Integer(compute='_compute_calls', string='# of Calls')

    @api.one
    def _compute_calls(self):
        call_data = self.env['asterisk.cdr'].search()
        for call in call_data:
            if self.id in [call.to_partner_id, call.from_partner_id]:
                self.call_count += 1
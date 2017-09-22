# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    call_count = fields.Integer(compute='_compute_sale_order_count', string='# of Calls')
    def _compute_sale_order_count(self):
        call_data = self.env['asterisk.cdr'].search([('to_partner_id', '=', self.id)])
        _logger.info("Calls %s" % call_data)
        self.call_count = 20

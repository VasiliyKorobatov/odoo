# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP


class ResPartner(models.Model):
    _inherit = 'res.partner'
    call_count = fields.Integer(compute='_compute_sale_order_count', string='# of Calls')
    def _compute_sale_order_count(self):
        call_data = self.env['asterisk.cdr'].search(['|',('to_partner_id', '=', self.id),('from_partner_id', '=', self.id)])
        self.call_count = len(call_data)

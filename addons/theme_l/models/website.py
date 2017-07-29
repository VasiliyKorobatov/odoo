# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def sale_categories(self):
        return list(self.env['product.public.category'].sudo().search([]))

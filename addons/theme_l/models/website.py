# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Website(models.Model):
    _inherit = "website"

    content_before = fields.Html("Content In Top")
    content_after = fields.Html("Content In Bottom")

    @api.model
    def sale_categories(self):
        return list(self.env['product.public.category'].sudo().search([]))


class WebsiteConfigSettings(models.TransientModel):

    _inherit = 'website.config.settings'

    content_before = fields.Html(related='website_id.content_before')
    content_after = fields.Html(related='website_id.content_after')

class Menu(models.Model):
    _inherit = "website.menu"
    icon = fields.Char('menu icon class')
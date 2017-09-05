# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
try:
    import slugify as slugify_lib
except ImportError:
    slugify_lib = None
import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)

class Faq(models.Model):
    _name = 'faq.faq'
    _description = 'FAQ'
    name = fields.Char('Question', size=255, required=True, index=True)
    answer = fields.HTML(string="Answer", index=True)
    is_popular = fields.Boolean(string="Popular question", default=False)


class Website(models.Model):
    _inherit = "website"
    @api.model
    def popular_faq(self):
        return list(self.env['faq.faq'].sudo().search([['is_popular', '=', True]]))

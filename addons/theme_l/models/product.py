# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    height = fields.Integer('Height')
    width = fields.Integer('Width')
    length = fields.Integer('Length')
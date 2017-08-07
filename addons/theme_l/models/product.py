# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'
    dimensions_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        help="Default Unit of Measure used for dimension."
    )

class ProductProduct(models.Model):
    _inherit = "product.product"
    height = fields.Integer('Height')
    width = fields.Integer('Width')
    length = fields.Integer('Length')
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Product(models.Model):
    _inherit = 'product.template'
    dimensions_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        help="Default Unit of Measure used for dimension."
    )
    default_variant = fields.Many2one(
        'product.product',
        'Default Variant',
        help='Default Variant of Product',
    )


class ProductProduct(models.Model):
    _inherit = "product.product"
    height = fields.Integer('Height')
    width = fields.Integer('Width')
    length = fields.Integer('Length')


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"
    # content_before = fields.Html(string="Content Before")
    # content_after = fields.Html(string="Content After")
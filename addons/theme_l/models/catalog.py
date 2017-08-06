# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class ProductCatalogType(models.Model):
    _name = 'product.catalog.type'
    name = fields.Char(string="Name", required=True)
    product_template = fields.Many2many('product.template', string="Product Template", ondelete='set null', index=True )
    product_templates = fields.One2many('product.template', inverse_name="catalog_type", string="Product Template", ondelete='set null', index=True )

class ProductCatalogModel(models.Model):
    _name = 'product.catalog.model'
    name = fields.Char(string="Name", required=True)
    product_product = fields.Many2many('product.product', string="Product Variant", ondelete='set null', index=True  )



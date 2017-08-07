# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class ProductCatalogType(models.Model):
    _name = 'catalog.type'
    name = fields.Char(string="Name", required=True)

class ProductCatalogModel(models.Model):
    _name = 'catalog.model'
    name = fields.Char(string="Name", required=True)
    catalog_type = fields.Many2one(comodel_name="catalog.type", string="Catalog Type", required=True, )
    product_product = fields.Many2many('product.product', string="Product Variant", ondelete='set null', index=True  )



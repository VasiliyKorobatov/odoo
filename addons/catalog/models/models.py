# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class ProductCatalogType(models.Model):
    _name = 'catalog.type'
    name = fields.Char(string="Name", required=True)

class ProductCatalogModel(models.Model):
    _name = 'catalog.model'
    name = fields.Char(string="Name", required=True)
    display_name = fields.Char(compute='_compute_display_name', store=True, index=True)
    catalog_type = fields.Many2one(comodel_name="catalog.type", string="Catalog Type", required=True, )
    product_product = fields.Many2many('product.product', 'mod_prod_rel', 'model_id', 'product_id', string="Product Variant", ondelete='set null', index=True  )

    def _compute_display_name(self):
        self.display_name = self.catalog_type.name+" "+self.name

class ProductProduct(models.Model):
    _inherit = "product.product"
    catalog_model_ids = fields.Many2many('catalog.model', 'mod_prod_rel', 'product_id', 'model_id',
                                       string="Model")


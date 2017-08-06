# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class ProductCatalogType(models.Model):
    _name = 'product.catalog.type'
    name = fields.Char(string="Name", required=True)

class ProductCatalogModel(models.Model):
    _name = 'product.catalog.model'
    name = fields.Char(string="Name", required=True)



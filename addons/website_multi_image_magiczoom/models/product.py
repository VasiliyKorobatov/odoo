# -*- coding: utf-8 -*-

from odoo import fields, models

class Product(models.Model):
    _inherit = "product.product"

    attribute_string = fields.Char('All Product attributes to String', compute='_compute_attribute_string')

    def _compute_attribute_string(self):
        attribute_value_ids = self.attribute_value_ids
        attribute_string = ''
        for attr in attribute_value_ids:
            attribute_string += ' '+attr.attribute_id.name+' '+attr.name
        self.attribute_string = attribute_string
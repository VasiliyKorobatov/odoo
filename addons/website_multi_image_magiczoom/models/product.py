# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Product(models.Model):
    _inherit = "product.product"

    attribute_string = fields.Char('All Product attributes to String', compute='_compute_attribute_string')
    @api.one
    def _compute_attribute_string(self):
        attribute_value_ids = self.attribute_value_ids
        attribute_string = ''
        attr_len = len(attribute_value_ids)
        for i, attr in enumerate(attribute_value_ids):
            attribute_string += attr.attribute_id.name+': '+attr.name
            if i < (attr_len-1):
                attribute_string += ', '
        self.attribute_string = attribute_string
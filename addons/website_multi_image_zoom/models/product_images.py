# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class ProductImage(models.Model):
    _name = 'product.image'
    _description = 'Product Image'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    image_alt = fields.Text(string='Image Label')
    image = fields.Binary(string='Image')
    image_small = fields.Binary(string='Small Image', compute='_compute_images')
    # image_small = fields.Binary(string='Small Image', compute='_compute_images', inverse='_set_image_small')
    image_url = fields.Char(string='Image URL')
    product_tmpl_id = fields.Many2one('product.template', 'Product',
                                      copy=False)
    product_variant_id = fields.Many2one('product.product', 'Product Variant',
                                         copy=False)

    @api.one
    @api.depends('image')
    def _compute_images(self):
        if self._context.get('bin_size'):
            self.image_small = self.image
        else:
            resized_images = tools.image_get_resized_images(self.image, return_big=True, avoid_resize_medium=True)
            self.image_small = resized_images['image_small']

    @api.one
    def _set_image_small(self):
        self._set_image_value(self.image_small)
    #
    # @api.one
    # def _set_image_value(self, value):
    #     image = tools.image_resize_image_big(value)
    #     if self.product_tmpl_id.image:
    #         self.image_variant = image
    #     else:
    #         self.product_tmpl_id.image = image


class ProductProduct(models.Model):
    _inherit = 'product.product'

    images_variant = fields.One2many('product.image', 'product_variant_id',
                                     'Images')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('product.image', 'product_tmpl_id', 'Images')
    variant_bool = fields.Boolean(string='Show Variant Wise Images',
                                  help='Check if you like to show variant wise'
                                       ' images in WebSite', auto_join=True)
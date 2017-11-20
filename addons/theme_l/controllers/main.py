# -*- coding: utf-8 -*-

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleOptions(WebsiteSale):

    @http.route(['/website/data/product'],  type='json',  methods=['POST'], auth="public", website=True)
    def product(self, product_id, **kwargs):
        p = request.env['product.product'].sudo().search([('id', '=', product_id)])
        # return {'website_price':p.website_price,'weight':p.weight,'volume':p.volume,'length':p.length,'width':p.width,'height':p.height,'default_code':p.default_code}
        return True
# -*- coding: utf-8 -*-

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    @http.route(['/data/product'],  type='json', auth="public", website=True)
    def product(self,  **kwargs):
        p = request.env['product.product'].sudo().search([('id', '=', kwargs.get('product_id'))])
        return {'website_price':p.website_price,'weight':p.weight,'volume':p.volume,'length':p.length,'width':p.width,'height':p.height,'default_code':p.default_code}

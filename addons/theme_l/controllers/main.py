# -*- coding: utf-8 -*-

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleOptions(WebsiteSale):

    @http.route(['/website/data/product'],  type='json',  methods=['POST'], auth="public", website=True)
    # def product(self, product_id, **kw):
    #     p = request.env['product.product'].sudo().search([('id', '=', product_id)])
    #     # return {'website_price':p.website_price,'weight':p.weight,'volume':p.volume,'length':p.length,'width':p.width,'height':p.height,'default_code':p.default_code}
    #     return True
    #
    # @http.route(['/shop/modal'], type='json', auth="public", methods=['POST'], website=True)
    def modal(self, product_id, **kw):
        pricelist = request.website.get_current_pricelist()
        product_context = dict(request.context)
        if not product_context.get('pricelist'):
            product_context['pricelist'] = pricelist.id
        # fetch quantity from custom context
        product_context.update(kw.get('kwargs', {}).get('context', {}))

        from_currency = request.env.user.company_id.currency_id
        to_currency = pricelist.currency_id
        compute_currency = lambda price: request.env['res.currency']._compute(from_currency, to_currency, price)
        product = request.env['product.product'].with_context(product_context).browse(int(product_id))
        return request.env['ir.ui.view'].render_template("website_sale_options.modal", {
            'product': product,
            'compute_currency': compute_currency,
            'get_attribute_value_ids': self.get_attribute_value_ids,
        })
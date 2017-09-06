# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo import api, fields, models
from odoo.http import request
from odoo.addons.website.models.website import slug

logger = logging.getLogger(__name__)

class Sitemap(http.Controller):
    @http.route('/sitemap', type='http', auth='public',
                website=True)
    def index(self, **kw):
        Faq = http.request.env['faq.faq']
        products = http.request.env['product.template'].search([['active','=',True]])
        pages = http.request.env['website.menu'].search([], order='url')
        values = Faq.search([])
        urls = {}
        category_product_urls = {}
        for product in products:
            for c_id in product.public_categ_ids:
                product_data = {'/shop/product/%s' % slug(product): product.name}
                if c_id.id not in category_product_urls.keys():
                    category_product_urls[c_id.id] = [product_data]
                else:
                    category_product_urls[c_id.id].append(product_data)
        for page in pages:
            if page.url == '/page/homepage' or page.url == '':
                continue
            if page.url not in urls:
                urls[page.url] = page.name
        url_map = []
        for k in sorted(urls.keys()):
            if '/shop/category/' not in k:
                url_map.append({k: [urls[k], []]})
            else:
                cat_id = k.split('-')[-1]
                url_map.append({k: [urls[k], category_product_urls[cat_id]]})
        logger.info(url_map)
        return http.request.render("faq.faqs", {
           'faqs': values
        })
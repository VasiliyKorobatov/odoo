# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo import api, fields, models
from odoo.http import request

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
                if c_id not in category_product_urls.keys():
                    category_product_urls[c_id] = [{product.website_url:product.name}]
                else:
                    category_product_urls[c_id].append({product.website_url:product.name})
        for page in pages:
            if page.url == '/page/homepage' or page.url == '':
                continue
            if page.url not in urls:
                urls[page.url] = page.name
        for k in sorted(urls.keys()):
            logger.info('%s:%s' % (k, urls[k]))
        logger.info(category_product_urls)
        return http.request.render("faq.faqs", {
           'faqs': values
        })
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
        locs = request.website.with_context(use_public_user=True).enumerate_pages()
        urls = []
        for page in pages:
            logger.info('%s:%s' % (page.url,page.name))
        return http.request.render("faq.faqs", {
           'faqs': values
        })
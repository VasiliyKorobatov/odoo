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
        values = Faq.search([])
        locs = request.website.with_context(use_public_user=True).enumerate_pages()
        urls = []
        for page in locs:
            urls.append(page['loc'])
        logger.info(urls)
        return http.request.render("faq.faqs", {
           'faqs': values
        })
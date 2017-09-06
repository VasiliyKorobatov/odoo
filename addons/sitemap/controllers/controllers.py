# -*- coding: utf-8 -*-
from odoo import http
from odoo import api, fields, models

class Sitemap(http.Controller):
    @http.route('/sitemap', type='http', auth='public',
                website=True)
    def index(self, **kw):
        Faq = http.request.env['faq.faq']
        values = Faq.search([])
        return http.request.render("faq.faqs", {
           'faqs': values
        })
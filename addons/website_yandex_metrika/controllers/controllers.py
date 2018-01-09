# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteYandexMetrika(http.Controller):
#     @http.route('/website_yandex_metrika/website_yandex_metrika/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_yandex_metrika/website_yandex_metrika/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_yandex_metrika.listing', {
#             'root': '/website_yandex_metrika/website_yandex_metrika',
#             'objects': http.request.env['website_yandex_metrika.website_yandex_metrika'].search([]),
#         })

#     @http.route('/website_yandex_metrika/website_yandex_metrika/objects/<model("website_yandex_metrika.website_yandex_metrika"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_yandex_metrika.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

class City(http.Controller):
    @http.route('/city', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/catalog/catalog/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('catalog.listing', {
#             'root': '/catalog/catalog',
#             'objects': http.request.env['catalog.catalog'].search([]),
#         })

#     @http.route('/catalog/catalog/objects/<model("catalog.catalog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('catalog.object', {
#             'object': obj
#         })
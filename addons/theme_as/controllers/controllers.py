# -*- coding: utf-8 -*-
from odoo import http

# class ThemeAs(http.Controller):
#     @http.route('/theme_as/theme_as/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_as/theme_as/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_as.listing', {
#             'root': '/theme_as/theme_as',
#             'objects': http.request.env['theme_as.theme_as'].search([]),
#         })

#     @http.route('/theme_as/theme_as/objects/<model("theme_as.theme_as"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_as.object', {
#             'object': obj
#         })
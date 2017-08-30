# -*- coding: utf-8 -*-
import werkzeug

from odoo import SUPERUSER_ID
from odoo import http
from odoo.http import request
from odoo.addons.website.models.website import slug

class City(http.Controller):
    @http.route('/city', auth='public')
    def index(self, **kw):
        values = []
        return http.request.render("city.cities", values)

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
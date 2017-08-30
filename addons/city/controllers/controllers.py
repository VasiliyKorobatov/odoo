# -*- coding: utf-8 -*-
import werkzeug

from odoo import SUPERUSER_ID
from odoo import http
from odoo.http import request
from odoo.addons.website.models.website import slug

class City(http.Controller):
    @http.route('/city', type='http', auth='public',
                website=True)
    def index(self, **kw):
        cities_ru = self.env['city.city'].search([['country_id.id','=','base.ru'],['address','!=',False]])
        cities_kz = []
        return http.request.render("city.cities", {'cities_ru':cities_ru})

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
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
        Cities = http.request.env['city.city']
        cities_ru = Cities.search([['address','!=',False],['country_id.code','=','RU']], order='name')
        cities_kz = Cities.search([['address','!=',False],['country_id.code','=','KZ']], order='name')
        return http.request.render("city.cities", {
            'cities_ru':cities_ru,
            'cities_kz':cities_kz,
        })

    @http.route(['/city/<model("city.city"):city>'],
                type='http', auth="public", website=True)
    def city(self, city, **kw):
        return http.request.render("city.detail", {
            "city": city
        })
# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
try:
    import slugify as slugify_lib
except ImportError:
    slugify_lib = None
import logging
import unicodedata
import re
from odoo.tools import ustr
from odoo import api, fields, models
from odoo.addons.website.models.website import slug
_logger = logging.getLogger(__name__)

class City(models.Model):
    _name = 'city.city'
    _description = 'City'

    @api.multi
    def name_get(self):
        res = []
        for line in self:
            name = line.name
            if line.zip:
                name = "%s %s" % (line.zip, name)
            if line.state_id:
                name = "%s, %s" % (name, line.state_id.name)
            if line.country_id:
                name = "%s, %s" % (name, line.country_id.name)
            res.append((line['id'], name))
        return res

    @api.one
    def _get_url(self):
        self.url = '/city/%s' % slug(self)

    @api.depends('name')
    def _slug_name(self):
        s = ustr(self.name)
        self.slug_name = slugify_lib.slugify(s)


    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        args = ['|', ('zip', operator, name), ('name', operator, name)]
        rec_ids = self.search(args, limit=limit)
        return rec_ids.name_get()


    state_id = fields.Many2one('res.country.state', 'State', index=True)
    name = fields.Char('City', size=64, required=True, index=True)
    zip = fields.Char('ZIP', size=64)
    country_id = fields.Many2one('res.country', 'Country', index=True)
    code = fields.Char('City Code', size=64,
                       help="The official code for the city")
    address = fields.Char('Address',
                       help="The official address in city")
    area_ids = fields.One2many('city.area', 'city_id', 'Area')
    std_code = fields.Char('STD Code', size=32)
    url = fields.Char(compute='_get_url')
    slug_name = fields.Char(compute='_slug_name')
    is_popular = fields.Boolean(string="Popular city", default=False)
    population = fields.Integer(string="City population", required=False, default=0)


class CityArea(models.Model):
    _name = 'city.area'
    _description = 'City'

    @api.multi
    def name_get(self):
        res = []
        for line in self:
            name = line.name
            if line.zip:
                name = "%s %s" % (line.zip, name)
            if line.city_id:
                name = "%s, %s" % (name, line.city_id.name)
            if line.city_id.state_id:
                name = "%s, %s" % (name, line.city_id.state_id.name)
            if line.city_id.country_id:
                name = "%s, %s" % (name, line.city_id.country_id.name)
            res.append((line['id'], name))
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        areas = self.search(['|', ('zip', 'ilike', name),
                             '|', ('name', 'ilike', name),
                             '|', ('code', 'ilike', name),
                             '|', ('city_id.name', 'ilike', name),
                             '|', ('city_id.code', 'ilike', name),
                             '|', ('city_id.zip', 'ilike', name),
                             '|', ('city_id.state_id.name', 'ilike', name),
                             '|', ('city_id.state_id.code', 'ilike', name),
                             ('city_id.country_id.code', 'ilike', name)],
                            limit=limit)
        if not areas:
            areas = self.search([('name', operator, name)], limit=limit)
        return areas.name_get()

    name = fields.Char('Area', size=256, required=True, index=True)
    zip = fields.Char('ZIP', size=256)
    city_id = fields.Many2one('city.city', 'City', index=True)
    code = fields.Char('Area Code', size=64,
                       help="The official code for the area")


class CountryState(models.Model):
    _inherit = 'res.country.state'

    city_ids = fields.One2many('city.city', 'state_id', 'Cities')


class ResPartner(models.Model):
    _inherit = "res.partner"

    area_id = fields.Many2one('city.area', 'Location')
    std_code = fields.Char(related="area_id.city_id.std_code",
                           string='STD Code', size=32)

    city_id = fields.Many2one('city.city', 'City Location')

    @api.onchange('city_id')
    def onchange_city_id(self):
        if self.city_id:
            self.city = self.city_id.name
            self.country_id = self.city_id.country_id.id
            self.state_id = self.city_id.state_id.id

    @api.onchange('area_id')
    def onchange_area_id(self):
        if self.area_id:
            self.zip = self.state_id = self.country_id = False
            self.zip = self.area_id.zip
            city = self.area_id.city_id
            if city and city.state_id:
                self.state_id = city.state_id.id
                if city.state_id.country_id:
                    self.country_id = city.state_id.country_id.id




class Website(models.Model):
    _inherit = "website"
    @api.model
    def popular_cities(self):
        return list(self.env['city.city'].sudo().search([['is_popular', '=', True]], order='population desc'))

    @api.model
    def all_cities(self):
        return list(self.env['city.city'].sudo().search([['country_id.code', 'in', ['RU','KZ']]], order='country_id desc, name'))

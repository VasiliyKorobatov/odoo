# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2014-2016 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models

class Company(models.Model):
    _inherit = 'res.company'

    inn = fields.Char(related='partner_id.inn')
    kpp = fields.Char(related='partner_id.kpp')
    okpo = fields.Char(related='partner_id.okpo')
    # ogrn = fields.Char(related='partner_id.ogrn')
    chief_id = fields.Many2one('res.users', 'Chief')
    accountant_id = fields.Many2one('res.users', 'General Accountant')
    print_facsimile = fields.Boolean('Print Facsimile', help="Check this for adding Facsimiles of responsible persons to documents.")
    print_stamp = fields.Boolean('Print Stamp', help="Check this for adding Stamp of company to documents.")
    stamp = fields.Binary("Stamp")
    print_anywhere = fields.Boolean('Print Anywhere', help="Uncheck this, if you want add Facsimile and Stamp only in email.", default=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
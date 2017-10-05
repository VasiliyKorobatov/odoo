# -*- encoding: utf-8 -*-
# Not Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'L theme',
    'description': 'L theme',
    'version': '0.1',
    'author': 'Vasiliy Korobatov',
    'data': [
        'views/assets.xml',
        'views/cart.xml',
        'views/layout.xml',
        'views/options.xml',
        'views/pages.xml',
        'views/views.xml',
        'views/snippets.xml'
    ],
    'category': 'Theme/Creative',
    'depends': ['website', 'website_sale', 'sale'],
    'application': False,
}

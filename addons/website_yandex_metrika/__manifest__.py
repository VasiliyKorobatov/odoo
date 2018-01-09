# -*- coding: utf-8 -*-
{
    'name': "Yandex.Metrika for website",

    'summary': """
        Install Yandex.Metrika Script""",

    'description': """
        Install Yandex.Metrika Script
    """,

    'author': "Vasiliy Korobatov",
    'website': "http://korobatov.ru",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
}
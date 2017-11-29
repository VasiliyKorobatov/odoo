# -*- coding: utf-8 -*-
{
    'name': "Website Fullscreen Menu Disable login ",

    'summary': """
        Fullscreen menu Disable login """,

    'description': """
        Fullscreen menu Disable login 
    """,

    'author': "Vasiliy Korobatov",
    'website': "http://korobatov.ru",

    'category': 'Website',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website',
                'website_fullscreen_menu'
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
}
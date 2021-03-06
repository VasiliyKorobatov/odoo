# -*- coding: utf-8 -*-
{
    'name': "theme_as",

    'summary': """
        Theme a.s.""",

    'description': """
        Simple Theme a.s.
    """,

    'author': "Vasiliy Korobatov",
    'website': "http://korobatov.ru",

    'category': 'Theme',
    'version': '10.0.0.1',

    'depends': ['base',
                'website',
                'website_fullscreen_menu',
                ],

    'data': [
        'views/assets.xml',
        'views/pages.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
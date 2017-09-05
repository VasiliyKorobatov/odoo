# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    "name": "FAQ",
    "version": "10.0.0.0.1",
    "author": "Vasiliy Korobatov",
    "category": "Website",
    "license": "AGPL-3",
    "summary": "FAQ",
    "description": """FAQs.""",
    "depends": ["website"],
    "data": [
        "views/faq_view.xml",
        "views/templates.xml",
        "security/ir.model.access.csv",
        ],
    "installable": True,
    "auto_install": False,
}

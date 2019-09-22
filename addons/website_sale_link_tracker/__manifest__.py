# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'eCommerce Link Tracker',
    'version': '1.0.190922',
    'description': """
View Link Tracker Statistics on eCommerce dashboard
=====================================================

        """,
    'depends': ['website_links', 'website_sale'],
    'data': [
        'views/sale_order_views.xml',
        'views/assets.xml',
    ],
    'demo': [
        'data/sale_order_demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'auto_install': True,
}

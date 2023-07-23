# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Nano Tech Soft LLC.
# See LICENSE file for full copyright and licensing details.
{
    'name': "Nanotsoft Partners Auto Reconcile",
    'category': 'Accounting/Accounting',
    'summary': """Nanotsoft Partners Auto Reconcile is easy to make your net off between partners.""",
    'version': '14.0.0.1',
    'author': "Nano Tech Soft LLC",
    'website': 'https://www.nanotsoft.com/',
    'sequence': 2,
    'description': """This module allows you to automatically reconcile all the customer invoices and vendor bills with just one click.""",
    'depends': ['account_reports'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/assets.xml',
    ],
    'qweb': [],
    'images' : ['static/description/banner.png'],
    'installable': True,
    'live_test_url': 'https://www.youtube.com/',
    'price': 47.99,
    'currency': 'USD',
    'auto_install': False,
    'application': False,
}

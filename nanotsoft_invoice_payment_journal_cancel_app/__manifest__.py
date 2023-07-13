# -*- coding: utf-8 -*-
{
    'name': 'Cancel Invoice, Payment, Journal, Reset to draft even Delete',
    "author": "Nano Tech Soft",
    'version': '14.0.1.1',
    'live_test_url': "https://youtu.be/uOSKKPrAzPY",
    "images":['static/description/main_screenshot.png'],
    "summary" : 'Cancel Invoice, Reset to Draft, Payment Cancel Journal Entry Cancel, Vendor Bill Cancel Bill Payment Cancel, All in One Account Cancel Delete accounting vouchers',
    'description': """ 
        Reset Invoice & Cancel | Cancel Payment |
    """,
    "license" : "OPL-1",
    'depends': ['base','sale_management'],
    'data': [ 
        'security/security.xml',
        'views/account_move_action.xml',
        'views/account_payment_action.xml',
        'views/account_move.xml',
        'views/account_payment.xml',
        'views/res_company.xml',
        'views/res_config_settings.xml',      
            ],
    'installable': True,
    'auto_install': False,
    'price': 12,
    'currency': "EUR",
    'category': 'Accounting',


}


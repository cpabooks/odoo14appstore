# -*- coding: utf-8 -*-
##############################################################################
#
#    Nano Tech Soft LLC
#    Copyright (C) 2018-TODAY JNano Tech Soft LLC (<http://www.nanotsoft.com>).
#    Author: Nano Tech Soft LLC (<http://www.nanotsoft.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'User Login History Tracker',
    'summary': "Have login History of users for the recent month.",
    'version': '14.0.0.1.0',
    'category': 'user',
    'author': 'Nano Tech Soft LLC',
    'maintainer': 'Nano Tech Soft LLC.',
    'contributors':['Nano Tech Soft LLC'],
    'website': 'https://www.nanotsoft.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_login_history_view.xml',
        'views/res_users_view.xml',
        'views/history_record_remover_cron.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/poster_image.png'],
    'price': 10.00,
    'currency': 'EUR',
}

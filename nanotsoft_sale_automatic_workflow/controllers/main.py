# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
_logger = logging.getLogger(__name__)


class WebsiteSaleAutoFlow(WebsiteSale):

    @http.route('/shop/payment/validate', type='http', auth="public", website=True, sitemap=False)
    def payment_validate(self, transaction_id=None, sale_order_id=None, **post):
        """ Method that should be called by the server when receiving an update
        for a transaction. State at this point :

         - UDPATE ME
        """
        if sale_order_id is None:
            order = request.website.sale_get_order()
        else:
            order = request.env['sale.order'].sudo().browse(sale_order_id)
            assert order.id == request.session.get('sale_last_order_id')

        order.sale_auto_payment_fims()
        if transaction_id:
            tx = request.env['payment.transaction'].sudo().browse(transaction_id)
            assert tx in order.transaction_ids()
        elif order:
            tx = order.get_portal_last_transaction()
        else:
            tx = None

        if not order or (order.amount_total and not tx):
            return request.redirect('/shop')

        if order and not order.amount_total and not tx:
            order.with_context(send_email=True).action_confirm()
            return request.redirect(order.get_portal_url())

        # clean context and session, then redirect to the confirmation page
        request.website.sale_reset()
        if tx and tx.state == 'draft':
            return request.redirect('/shop')

        PaymentProcessing.remove_payment_transaction(tx)
        return request.redirect('/shop/confirmation')
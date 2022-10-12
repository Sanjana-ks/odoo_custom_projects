# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string='Discount Amount')


class UpdateFieldInvoice(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    _description = 'Update the custom field value from sale order to invoice'

    def create_invoices(self):
        res = super(UpdateFieldInvoice, self).create_invoices()
        active_id = self._context.get('active_id')
        print(active_id)
        if active_id:
            sale_order_id = self.env['sale.order'].browse(active_id)
            invoice_id = self.env['account.move'].search([('invoice_origin', '=', sale_order_id.name)])
            lst = []
            index = 0
            for rec in sale_order_id.order_line:
                lst.append(rec.discount_amount)
            for val in invoice_id.invoice_line_ids:
                val.write({'discount_amount': lst[index]})
                index += 1

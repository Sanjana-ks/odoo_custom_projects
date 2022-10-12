# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomVendorBillLine(models.Model):
    _inherit = 'account.move'

    custom_vendor_bill_line = fields.One2many('vendor.bill.line', 'vendor_bill_id', string='Custom Invoice Lines')


class SaleInvoiceLine(models.Model):
    _inherit = "account.move.line"

    discount_amount = fields.Float(string='Discount Amount')


class VendorBillLine(models.Model):
    _name = 'vendor.bill.line'
    _description = 'Vendor Bill Line'

    def _calculate_subtotal(self):
        for val in self:
            val.subtotal = val.quantity * val.price

    vendor_bill_id = fields.Many2one('account.move')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1)
    price = fields.Float(string='Unit Price')
    subtotal = fields.Float(string='Sub Total', compute='_calculate_subtotal')

    @api.onchange('product_id')
    def onchange_product_price(self):
        print("onchange")
        if self.product_id:
            self.price = self.product_id.standard_price

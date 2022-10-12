# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order'

    custom_product_line = fields.One2many('custom.product.details', 'custom_product_id', string='Product')

    def send_bill(self):
        self.name
        # print(ref_id)
        if self.name:
            res = self.env['account.move'].search([('invoice_origin', '=ilike', self.name)])
            print(res)
            lst = []
            res.custom_vendor_bill_line.unlink()
            for rec in self.custom_product_line:
                lst.append((0, 0, {'product_id': rec.product_id.id, 'quantity': rec.quantity,
                                   'price': rec.unit_price, 'subtotal': rec.subtotal}))
            print("list", lst)
            res['custom_vendor_bill_line'] = lst


class CustomProductDetails(models.Model):
    _name = 'custom.product.details'
    _description = 'Custom Product Details'

    def _calculate_subtotal(self):
        for val in self:
            val.subtotal = val.quantity * val.unit_price

    custom_product_id = fields.Many2one('purchase.order', string='Custom Product')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1)
    unit_price = fields.Float(string='Unit Price')
    subtotal = fields.Float(string='Sub Total', compute='_calculate_subtotal')

    @api.onchange('product_id')
    def onchange_product_price(self):
        print("onchange")
        if self.product_id:
            self.unit_price = self.product_id.list_price

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductWizard(models.TransientModel):
    _name = 'product.wizard'
    _description = 'Wizard of Product Details'

    product_line = fields.One2many('custom.product.wizard', 'custom_product_id', string='Product Details')

    @api.model
    def default_get(self, fields_list=[]):
        res = super(ProductWizard, self).default_get(fields_list)
        active_id = self._context.get('active_id')
        if active_id:
            purchase_id = self.env['purchase.order'].browse(active_id)
            lst = []
            for rec in purchase_id.order_line:
                lst.append(
                    (0, 0, {'product_id': rec.product_id.id, 'quantity': rec.product_qty,
                            'unit_price': rec.price_unit, 'subtotal': rec.price_subtotal}))
            res['product_line'] = lst
        return res

    def save_data(self):
        active_id = self._context.get('active_id')
        if active_id:
            res = self.env['purchase.order'].browse(active_id)
            lst = []
            for rec in res.custom_product_line:
                rec.unlink()
            for rec in self.product_line:
                lst.append((0, 0, {'product_id': rec.product_id.id, 'quantity': rec.quantity,
                                   'unit_price': rec.unit_price, 'subtotal': rec.subtotal}))
            print("list", lst)
            res['custom_product_line'] = lst
            return res


class ProductWizardLine(models.TransientModel):
    _name = 'custom.product.wizard'
    _description = 'Product Details Wizard'

    custom_product_id = fields.Many2one('product.wizard', string='Custom Product')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1)
    unit_price = fields.Float(string='Unit Price')
    subtotal = fields.Float(string='Sub Total')

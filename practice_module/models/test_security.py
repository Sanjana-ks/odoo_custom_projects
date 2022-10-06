# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Testing(models.Model):
    _name = "test"
    _description = "Testing Security"

    name = fields.Char(string='Test')
    test_description = fields.Char(string='Test Description')
    related_user = fields.Many2one('res.users', string="Related User")  # for record rule

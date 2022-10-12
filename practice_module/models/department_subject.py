# -*- coding: utf-8 -*-

from odoo import api, fields, models


# Department Class
class Department(models.Model):
    _name = 'department'
    _description = 'Department Names'

    name = fields.Char(string='Department')
    head = fields.Char(string='Head of Department')
    fees = fields.Integer(string='Fees (in Rs.)')
    subjects = fields.One2many('subject', 'department_id', string='Subjects')
    student_id = fields.One2many('student', 'department_id', string='Students')


# Subject Class
class Subject(models.Model):
    _name = 'subject'
    _description = 'Subject Names'

    department_id = fields.Many2one('department', string='Department')
    name = fields.Char(string='Subject')
    head = fields.Char(string="Head of Department")

    # #orm methods
    @api.onchange('department_id')
    def onchange_department_id(self):
        print("onchange")
        if self.department_id:
            if self.department_id.head:
                self.head = self.department_id.head
        else:
            self.head = ''

# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student"
    _description = "Student Data"

    def _calculate_remaining_fees(self):
        for val in self:
            if val.paid_fees:
                val.remaining_fees = val.fees - val.paid_fees
            else:
                val.remaining_fees = val.fees

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')], string='Gender')
    dob = fields.Date(string='DOB')
    mobile = fields.Char(string='Contact no.')
    department_id = fields.Many2one('department', string='Department')
    fees = fields.Integer(string='Fees(in Rs.)')
    paid_fees = fields.Integer(string='Fees Paid')
    remaining_fees = fields.Integer(string='Remaining Fees', compute='_calculate_remaining_fees')
    admission = fields.Datetime(string="Admission Date/Time")
    is_graduated = fields.Boolean(string='Is graduated?')
    document = fields.Binary(string='Upload Document')
    student_marks_line = fields.One2many('marks', 'student_id', string='Student Marks')
    student_subject_ids = fields.Many2many('subject', 'student_subject_rel', 'student_id', 'subject_id',
                                           string='Subjects')

    @api.onchange('department_id')
    def onchange_department_id_fees(self):
        print("onchange")
        if self.department_id:
            self.fees = self.department_id.fees

    # if the student is already graduated, form will not edit
    def write(self, vals):
        if self.is_graduated:
            return
        else:
            res = super(Student, self).write(vals)
            return res

# python constraints
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            student_name = self.env['student'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if student_name:
                raise ValidationError('Student name %r already exists' % rec.name)

# sql constraints
    _sql_constraints = [
        ('unique_mobile_number', 'unique(mobile)', 'Mobile number already exists in another record')
    ]

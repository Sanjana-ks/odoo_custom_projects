# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StudentExcel(models.TransientModel):
    _name = "student.excel"
    _description = "Student Excel Wizard"

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
    remaining_fees = fields.Integer(string='Remaining Fees')
    admission = fields.Datetime(string="Admission Date/Time")
    is_graduated = fields.Boolean(string='Is graduated?')

    @api.model
    def default_get(self, fields_list):
        res = super(StudentExcel, self).default_get(fields_list)
        print(res)
        active_id = self._context.get('active_id')
        rec = self.env['student'].browse(active_id)
        if active_id:
            print(active_id)
            print(rec)
            res['name'] = rec.name
            res['last_name'] = rec.last_name
            res['gender'] = rec.gender
            res['dob'] = rec.dob
            res['mobile'] = rec.mobile
            res['department_id'] = rec.department_id.id
            res['fees'] = rec.fees
            res['paid_fees'] = rec.paid_fees
            res['remaining_fees'] = rec.remaining_fees
            res['admission'] = rec.admission
            res['is_graduated'] = rec.is_graduated
        print(res)
        return res

    def print_excel(self):
        print('excel printing..........')
        data = {
            'form_data': self.read()[0]
        }
        return self.env.ref('practice_module.report_student_report_excel').report_action(self, data=data)


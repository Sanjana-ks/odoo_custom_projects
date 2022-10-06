# -*- coding: utf-8 -*-

from odoo import models


class StudentRecordExcel(models.AbstractModel):
    _name = "report.practice_module.report_student_record_excel"
    _inherit = "report.odoo_report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, student):
        print('..........', data['form_data'], student)
        sheet = workbook.add_worksheet('Excel Student Report')
        bold = workbook.add_format({'bold': True})
        row = 0
        col = 0
        sheet.write(row, col, 'Name', bold)
        sheet.write(row, col+1, 'Last Name', bold)
        sheet.write(row, col+2, 'Date of Birth', bold)
        sheet.write(row, col+3, 'Gender', bold)
        sheet.write(row, col+4, 'Contact No.', bold)
        sheet.write(row, col+5, 'Department', bold)
        sheet.write(row, col+6, 'Graduated?', bold)
        sheet.write(row, col+7, 'Admission', bold)
        sheet.write(row, col+8, 'Fees', bold)
        sheet.write(row, col+9, 'Paid Fees', bold)
        sheet.write(row, col+10, 'Remaining Fees', bold)

        row += 1
        sheet.write(row, col, student.name)
        sheet.write(row, col+1, student.last_name)
        sheet.write(row, col+2, data['form_data']['dob'])
        sheet.write(row, col+3, student.gender)
        sheet.write(row, col+4, student.mobile)
        sheet.write(row, col+5, student.department_id.name)
        sheet.write(row, col+6, student.is_graduated)
        sheet.write(row, col+7, data['form_data']['admission'])
        sheet.write(row, col+8, student.fees)
        sheet.write(row, col+9, student.paid_fees)
        sheet.write(row, col+10, student.remaining_fees)

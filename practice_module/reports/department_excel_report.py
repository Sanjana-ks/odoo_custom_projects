# -*- coding: utf-8 -*-

from odoo import models


class DepartmentRecordExcel(models.AbstractModel):
    _name = "report.practice_module.report_department_record_excel"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, department):
        data = {}
        print('..........', department)
        sheet = workbook.add_worksheet('Excel Department Report')
        bold = workbook.add_format({'bold': True})
        row = 0
        col = 0
        sheet.write(row, col, 'Department Name', bold)
        sheet.write(row, col + 1, 'HOD', bold)
        sheet.write(row, col + 2, 'Fees', bold)
        sheet.write(row, col + 3, 'Subjects', bold)
        row += 1
        sheet.write(row, col, department.name)
        sheet.write(row, col + 1, department.head)
        sheet.write(row, col + 2, department.fees)

        print(department.subjects)
        row = 1
        col = 3
        for subject in department.subjects:
            sheet.write(row, col, subject['name'])
            row += 1

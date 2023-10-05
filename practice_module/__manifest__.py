# -*- coding: utf-8 -*-

{
    'name': 'Practice Module',
    'version': '16.1.1',
    'sequence': '1',
    'category': 'Git Submodule Check ',
    'summary': 'Learning Odoo',
    'description': 'This is the practice module on working with odoo. Testing this module.',
    'depends': ["base", 'report_xlsx'],
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/department_subject_view.xml",
        "views/student_view.xml",
        "views/test_security.xml",
        "wizards/student_excel_wizard_view.xml",
        "views/menu_view.xml",
        "reports/reports.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Marks(models.Model):
    _name = "marks"
    _description = "Subject Marks"

    def _calc_percent(self):
        for val in self:
            total = val.physics_marks + val.chemistry_marks + val.maths_marks + val.english_marks
            percentage = total/4
            val.percent = percentage

    def _calc_total(self):
        for val in self:
            total = val.physics_marks + val.chemistry_marks + val.maths_marks + val.english_marks
            val.total = total

    student_id = fields.Many2one('student', string='Student Name')
    class_name = fields.Selection([
        ('class_x', '10th'),
        ('class_xii', '12th')], string='Class')
    physics_marks = fields.Float(string='Physics Marks')
    chemistry_marks = fields.Float(string='Chemistry Marks')
    maths_marks = fields.Float(string='Maths Marks')
    english_marks = fields.Float(string='English Marks')
    total = fields.Float(string='Total Marks', compute='_calc_total')
    percent = fields.Float(string='Percentage', compute='_calc_percent')

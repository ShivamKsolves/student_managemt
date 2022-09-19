from odoo import api, fields, models, _, tools


class StudentSubject(models.Model):
    _name = "student.subject"
    _description = "Student Subject"

    name = fields.Char(string='Subject')

    # student_id = fields.Many2one('student.student', string='Student')

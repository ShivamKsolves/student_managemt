from odoo import api, fields, models, _, tools


class StudentResult(models.Model):
    _name = "student.result"
    _description = "Student Result"

    subject_id = fields.Many2one('student.subject', string='Subject Id')
    total_marks = fields.Float(string='Total Marks')
    marks_obtain = fields.Float(string='Marks Obtain')
    pass_fail = fields.Selection([('pass','Pass'),('fail','Fail')],string='Pass Or Fail')
    # THis student_id field we will pass inside the One2many field inside which is present in student.student model
    student_id = fields.Many2one('student.student',string='Student Id')

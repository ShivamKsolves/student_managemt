from odoo import api, fields, models, _, tools


class UpdateDataWizard(models.TransientModel):
    _name = "update.data"
    _description = "Update Of Student Data"

    subject_id = fields.Many2one('student.subject', string='Subject')
    total_marks = fields.Float(string='Total Marks')
    marks_obtain = fields.Float(string='Marks Obtain')
    pass_fail = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], string='Pass Or Fail')

    # student_result_ids = fields.One2many('student.result', 'student_id')

    def action_update(self):
        for order in self:
            active_id = self._context.get('active_id')
            student = self.env['student.student'].search([('id', '=', active_id)])
            if active_id:
                data = {'subject_id': order.subject_id.id, 'marks_obtain': order.marks_obtain,
                        'total_marks': order.total_marks, 'pass_fail': order.pass_fail,
                        'student_id': active_id}

                self.env['student.result'].create(data)

    # def action_update(self):
    #     for order in self:
    #         active_id = self._context.get('active_id')
    #         if active_id:
    #             active_id = order.env['student_result_ids'].create({
    #                 'subject_id': order.subject_id,
    #                 'marks_obtain': order.marks_obtain,
    #                 'total_marks': order.total_marks,
    #                 'pass_fail': order.pass_fail,
    #             })

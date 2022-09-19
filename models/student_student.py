from datetime import date

from _cffi_backend import string
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student Student"

    name = fields.Char(string='Student Name', required=True)
    father_name = fields.Char(string='Father Name')
    blood_group = fields.Char(string='Blood Group')
    email = fields.Char(string='Email', required=True)
    age = fields.Integer(string='Age')
    subject_ids = fields.Many2many('student.subject')
    student_result_ids = fields.One2many('student.result', 'student_id')
    date_of_birth = fields.Date(string='Dob')
    result = fields.Char(string='Result', compute='_compute_result', tracking=True)
    student_img = fields.Image("Student Image")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    branch = fields.Selection(
        [('cs', 'ComputerScience'), ('iT', 'Information & Technology'), ('civil', 'Civil'), ('me', 'Mechanical'),
         ('ec', 'Electronic Communication'), ('ch', 'Chemical Engineering')], string='Branch')
    state = fields.Selection([
        ('draft', 'draft'),
        ('admit', 'admitted'),
        ('transfered', 'transfered'),
        ('cancel', 'Cancelled'),
        ('done', 'Closed'),
    ], string='Status', readonly=True, copy=False, index=True, default='draft')

    # _sql_constraints = [
    #     ('email_uniq', 'unique (email)', 'This email already exists')
    # ]

    def action_admitted(self):
        self.state = 'admit'
        return self

    # After clicking  the button which states will go
    def action_cancel(self):
        self.state = 'cancel'
        return self


    def action_set_to_draft(self):
        # Odoo search method
        student=self.env['student.student'].search([])
        print('students.............',student)

        # Search with and operation
        # female_student = self.env['student.student'].search([('gender','=','male'),('age','<=',21)])
        # print('Female_student....',female_student)

        # Search with Or operation
        # female_student = self.env['student.student'].search(['|',('gender', '=', 'female'), ('age', '<=', 21)])
        # print('Female_student....',female_student)

        # search count
        # student_count = self.env['student.student'].search_count([])
        # print('student_count =',student_count)
        # female_student_count = self.env['student.student'].search_count(['|', ('gender', '=', 'female'), ('age', '<=', 21)])
        # print('male and female student count....', female_student_count)
        # reference method
        # student_manage=self.env.ref('__export__.student_subject_6_cf115f84')
        # print('student_management....',student_manage.id)
        # browse method
        # student_browse = self.env['student.student'].browse(1)
        # print('student_broswe....', student_browse)
        # Here check record present or not
        # here i checked exists() method
        # if student_browse.exists():
        #     print('Record existing')
        # else:
        #     print('Record not existing')

        vals = {
            'name': 'M1'
        }
        # self.env['student.subject'].create(vals)
        # val={
        #     'name':'BIG Data'
        # }
        # subject_update=self.env['student.subject'].browse(16)
        # if subject_update.exists():
        #     subject_update.write(val)

        #  copy of the record
        # subject_name_copy=self.env['student.subject'].browse(16)
        # subject_name_copy.copy()
    #     unlink in odoo
    #     subject_unlink = self.env['student.subject'].browse(16)
    #     subject_unlink.unlink()

    # After clicking  the button which states will go
    # def action_set_to_draft(self):
    #     self.state = 'draft'
    #     return self

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth > date.today():
                raise ValidationError("Date of birth cannot in future date !!!")

    @api.onchange('date_of_birth')
    def onchange_date_of_birth(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
                if (rec.age > 0):
                    rec.age = rec.age
                else:
                    rec.age = 0
            else:
                rec.age = 0

    # _sql_constraints=[
    #     ('unique_email_name','unique(email)','This email already  exits')
    # ]
    # _sql_constraints = [
    #     ("project_task_unique_email", "UNIQUE (email)", _("Email must be unique!")),
    # ]

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            student = self.env['student.student'].search([('email', '=', rec.email), ('id', '!=', rec.id)])
            if student:
                raise ValidationError(_("This email  %s already exits" % rec.email))

    def _compute_result(self):
        total = 0
        obtained = 0
        for rec in self.student_result_ids:
            total = total + rec.total_marks
            obtained = obtained + rec.marks_obtain
        self.result = str(obtained) + '/' + str(total)

    # def _compute_result(self):
    #     for rec1 in self.student_result_ids:
    #         total = 0
    #         obtained = 0
    #         # for rec in self.student_result_ids:
    #         total = total + rec1.total_marks
    #         obtained = obtained + rec1.marks_obtain
    #     self.result = str(obtained) + '/' + str(total)

    # for rec in self.student_result_ids:
    #     percentage = (rec.total_marks * rec.marks_obtain) / 100
    #     if percentage >= 60:
    #         rec.result = 'First'
    #     elif percentage >= 45:
    #         rec.result = 'Second'
    #     elif percentage >= 30:
    #         rec.result = 'Third'
    #     else:
    #         rec.result = 'Fail'

from sqlite3 import Date

import xlrd
import logging
import tempfile
import binascii
from datetime import date, datetime, time
from odoo import api, fields, models, tools, _
from odoo.exceptions import Warning, UserError, ValidationError
from pyparsing import Char

_logger = logging.getLogger(__name__)

try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')


class ImportStudentWiz(models.TransientModel):
    _name = 'import.student.wiz'
    _description = 'Import Student Wizard'

    file = fields.Binary(string="Student Record Import")

    def import_student(self):
        if not self.file:
            raise ValidationError(_("Please Upload File to Student !"))

        try:
            file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            file.write(binascii.a2b_base64(self.file))
            file.seek(0)
            values = {}
            workbook = xlrd.open_workbook(file.name)
            sheet = workbook.sheet_by_index(0)
            print(sheet)
        except Exception:
            raise ValidationError(_("Please Select Valid File Format !"))
        student_obj = self.env['student.student']
        student_res = self.env['student.subject']
        for row_no in range(sheet.nrows):
            val = {}
            if row_no <= 0:
                fields = list(map(lambda row: row.value.encode('utf-8'), sheet.row(row_no)))
            else:
                line = list(
                    map(lambda row: isinstance(row.value, bytes) and row.value.encode('utf-8') or str(row.value),
                        sheet.row(row_no)))
                print(line[5])
                # print(line[10])
                # print(line[11])
                # print(line[12])
                print(line)
                # student_obj.create({'name': line[0]})
                subject_name=line[9]
                print(subject_name)
                student_rec = student_res.search([('name', '=', subject_name)], limit=1)
                print(student_rec)
                stu_val = {
                    'name': line[0],
                    'gender': line[1],
                    'father_name': line[2],
                    'blood_group': line[3],
                    # 'age': float(line[4]),
                    # 'date_of_birth': line[5],
                    # 'result': Char(line[6]),
                    'branch': line[7],
                    'email': line[8],
                    'student_result_ids':
                        [(0, 0, {'subject_id': student_rec.id,
                                 'total_marks': line[10],
                                 'marks_obtain': line[11],
                                 'pass_fail': line[12],
                                 })]
                }
                # student_obj.create({'inv_val': line[0]})
                student_obj.create(stu_val)


                # stu_rec.env['student.result'].create(stu_rec2)
                # stu_rec.env[student_res].create(stu_rec2)
                # student_res.env[stu_rec].create(stu_rec2)

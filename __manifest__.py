{
    'name': 'student_Management',
    'version': '1.0',
    'category': 'Student',
    'summary': 'student Management System',
    'depends': ['base', 'sale'],
    'description': """ """,
    'data': [
        'security/ir.model.access.csv',
        'data/student.subject.csv',
        'wizard/update_result_view.xml',
        'wizard/student_import_view.xml',
        'views/student_view.xml',
        'views/menu.xml',
        'views/sale_order_view.xml',
        'report/student_report.xml',
        'report/sale_report_inherit.xml',


    ],
}

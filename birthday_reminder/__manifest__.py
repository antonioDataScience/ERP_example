# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source ERP Solution
#    Author: Antonio (AKD d.o.o.)

{
    'name': "Birthday Reminder",
    'description': """
        Long description of module's purpose
    """,
    'author': "Uvid",
    'website': "https://odoo.com.hr/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['hr'],
    'data': [
        'views/hr.xml',
        'views/birthday.xml',
        'report/report_birthday.xml',
        'data/cron.xml',
    ],
    'installable': True,
}
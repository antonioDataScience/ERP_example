# -*- coding: utf-8 -*-
{
    'name': "Transport",

    'summary': """
        Training for AKD""",

    'description': """
         Nothing special.
    """,

    'author': "Antonio Tolic",
    'website': "http://www.AKD.hr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/transport_views.xml',
        'views/relations.xml',
        'views/travels.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

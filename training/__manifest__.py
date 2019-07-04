# -*- coding: utf-8 -*-
{
    'name': "training",

    'summary': """
        Training module for AKD""",

    'description': """
        Long description for training module for AKD
    """,

    'author': "Uvid",
    'website': "http://www.odoo.com.hr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/training_sequence.xml',
        'views/training_views.xml',
        'views/training_location.xml',
        'views/hr.xml',
        'report/report_training.xml',
        'wizard/wizard_stock_inventory_view.xml',
        'report/report_training_list.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
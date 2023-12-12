# -*- coding: utf-8 -*-
{
    'name': "test_techinal_odoo",

    'summary': """
        Addons for test techinal odoo""",
    

    'description': """
        Addons for test techinal odoo
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material_view.xml',
        'views/res_partner_view.xml',
        'views/prime_number_view.xml',
        'views/digit_finder_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

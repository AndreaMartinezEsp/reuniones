# -*- coding: utf-8 -*-
{
    'name': "reuniones",

    'summary': "Esto es un módulo para gestionar las salas de reuniones",

    'description': """
    En este módulo guardaremos la información de las salas y las reuniones que se celebrarán en ellas
    """,

    'author': "AndreaMar",
    'website': "https://www.andreamar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reunion_view.xml',
        'views/sala_view.xml'
        ,
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license': 'LGPL-3'
}


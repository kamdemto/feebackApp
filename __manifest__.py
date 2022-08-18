# -*- coding: utf-8 -*-
{
    'name': "restofeedback",

    'summary': "Ce module permet de receuillir les differents feedback des clients après une consommation",
    'sequence': 10,

    'description': "Sondage clientéle sur la qualité , le Goût et la quantité de repas qui leur est servi, Elle permet aussi d'avoir une vue d'ensemble sur la qualite du service fournir au client",

    'author': "HILATECH CO",
    'website': "http://www.hilatech.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Service',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'mail', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

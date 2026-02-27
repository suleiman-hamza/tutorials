# -*- coding: utf-8 -*-
{
    'name': "Estates",
    'summary': "Real Estate module tutorial",
    'description': "Real Estate module tutorial",
    'version': '19.0.0.1',
    'application': True,
    'installable': True,
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml', #action
        'views/estate_menus.xml',
    ],
    'author': 'Suleiman Hamza',
    'license': 'LGPL-3',
}
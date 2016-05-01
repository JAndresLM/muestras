# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Gestión de Boletas y Muestras",
    'summary': """Control de las muestras del laboratorio de analisis agronomicos""",
    'author': "Andrés López, Mauricio Rodríguez & Carlos Solis",
    'website': "http://www.andmaca.blogspot.com",
    'category': 'Agronomía',
    'version': '8.0.1',
    'depends': ['base','clientes'],
    'data': [
        'views/menu.xml',
        'views/report.xml',
        'views/ticket.xml',
        'views/crop.xml',
        'views/sample.xml',
        'views/category.xml',
        'views/analysis.xml',
        'views/element.xml',
    ],
    'demo': [
        'demo.xml',
    ],
}

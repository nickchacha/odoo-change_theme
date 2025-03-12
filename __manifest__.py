{
    'name': 'Complete Debranding for Odoo 16',
    'version': '1.0',
    'depends': ['web', 'point_of_sale'],
    'data': ['views/debranding_views.xml'],
    'assets': {
    'web.assets_backend': [
        'my_debranding/static/src/img/logo.png',
        'my_debranding/static/src/js/debranding.js',
    ],
    'point_of_sale.assets': [
        'my_debranding/static/src/img/logo.png',
    ],
},
    'installable': True,
    'auto_install': False,
}
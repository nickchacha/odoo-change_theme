{
    'name': 'Complete Debranding for Odoo 16',
    'version': '1.0',
    'depends': ['web', 'point_of_sale'],
    'data': ['views/login_templates.xml'],
    'assets': {
    'web.assets_backend': [
        'change_theme/static/src/img/logo.png',
        'change_theme/static/src/js/debranding.js',
        'change_theme/static/src/pos/chrome.xml',
        
    ],
    'point_of_sale.assets': [
        'change_theme/static/src/img/logo.png',

    ],
},
    'installable': True,
    'auto_install': False,
}
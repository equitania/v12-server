{
    'name': "Password Policy",
    "summary": "Implements basic password policy configuration & check",
    'version' : '1.0.191215',
    'depends': ['base_setup', 'web'],
    'data': [
        'data/defaults.xml',
        'views/assets.xml',
        'views/res_users.xml',
        'views/res_config_settings_views.xml',
    ]
}

# -*- coding: utf-8 -*-
{
    'name': "index_api_base",

    'summary': """
        Synchronisation de donnée de deux serveur""",

    'description': """
        Synchronisation de donnée de deux serveur:
        - Produit
        - Utilisateur
        - Vente POS
        -Stock picking
    """,

    'author': "IndexMada",
    'website': "http://index-mada.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'index_api_base'],

    # # always loaded
    # 'data': [
    #     'security/ir.model.access.csv',
    #     'views/config_settings_views.xml',
    #     'views/pos_session_views.xml',
    #     'data/cron.xml',
    # ],
}
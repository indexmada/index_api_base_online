from odoo import models, fields, api, _

class PosSession(models.Model):
    _inherit = "pos.session"

    external_id = fields.Integer(string="ID distant", help="ID de la session dans la base de données distante")
from odoo import models, fields, api, _

class PosOrder(models.Model):
    _inherit = "pos.order"

    external_id = fields.Integer(string="ID Externe", help="ID de la commande dans la base distante")
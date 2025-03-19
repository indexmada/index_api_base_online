from odoo import models, fields, api, _

class PosOrder(models.Model):
    _inherit = "pos.order"

    sent_to_api = fields.Boolean(string="Envoyé", default=False)
    external_id = fields.Integer(string="ID Externe", help="ID de la commande dans la base distante")
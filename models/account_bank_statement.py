from odoo import models, fields, api, _

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    external_id = fields.Integer(string="ID Externe", help="ID du relevé de caisse dans la base distante")
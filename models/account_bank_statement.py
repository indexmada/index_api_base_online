from odoo import models, fields, api, _

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    external_id = fields.Integer(string="ID Externe", help="ID du relevé de caisse dans la base distante")


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    statement_pos_order_name = fields.Char(string="POS Order Name", help="Nom de la commande POS associée à cette ligne de relevé bancaire.")
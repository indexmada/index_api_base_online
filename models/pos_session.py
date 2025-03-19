# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import xmlrpc.client

class PosSession(models.Model):
    _inherit = "pos.session"

    external_id = fields.Integer(string="ID distant", help="ID de la session dans la base de données distante")
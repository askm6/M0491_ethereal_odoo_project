# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    twitter_x_url = fields.Char(
        string="Twitter/X",
        help=(
            "URL del perfil de Twitter/X del cliente. "
            "Ej: https://x.com/usuario"
        ),
    )
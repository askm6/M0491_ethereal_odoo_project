# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    instagram_url = fields.Char(
        string="Instagram",
        help=(
            "URL del perfil de Instagram del cliente. "
            "Ej: https://www.instagram.com/usuario"
        ),
    )
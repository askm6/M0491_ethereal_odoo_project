# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    linkedin_url = fields.Char(
        string="LinkedIn",
        help=(
            "URL del perfil de LinkedIn del cliente. "
            "Ej: https://www.linkedin.com/in/usuario"
        ),
    )
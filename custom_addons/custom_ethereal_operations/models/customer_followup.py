# -*- coding: utf-8 -*-
from odoo import fields, models


class EtherealCustomerFollowup(models.Model):
    _name = "ethereal.customer.followup"
    _description = "Seguimiento de cliente ETHEREAL"
    _order = "followup_date desc"

    name = fields.Char(
        string="Referencia",
        required=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Cliente",
        required=True,
    )
    followup_date = fields.Date(
        string="Fecha de seguimiento",
        default=fields.Date.context_today,
        required=True,
    )
    channel = fields.Selection(
        [
            ("email", "Correo electrónico"),
            ("instagram", "Instagram"),
            ("linkedin", "LinkedIn"),
            ("twitter_x", "Twitter/X"),
            ("website", "Tienda online"),
            ("other", "Otro"),
        ],
        string="Canal de contacto",
        default="website",
        required=True,
    )
    priority = fields.Selection(
        [
            ("low", "Baja"),
            ("normal", "Normal"),
            ("high", "Alta"),
            ("urgent", "Urgente"),
        ],
        string="Prioridad",
        default="normal",
        required=True,
    )
    state = fields.Selection(
        [
            ("new", "Nuevo"),
            ("in_progress", "En progreso"),
            ("done", "Finalizado"),
            ("cancelled", "Cancelado"),
        ],
        string="Estado",
        default="new",
        required=True,
    )
    notes = fields.Text(
        string="Notas",
    )
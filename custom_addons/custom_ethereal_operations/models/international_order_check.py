# -*- coding: utf-8 -*-
from odoo import fields, models


class EtherealInternationalOrderCheck(models.Model):
    _name = "ethereal.international.order.check"
    _description = "Control de pedido internacional ETHEREAL"
    _order = "check_date desc"

    name = fields.Char(
        string="Referencia de control",
        required=True,
    )
    sale_order_id = fields.Many2one(
        "sale.order",
        string="Pedido de venta",
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Cliente",
    )
    check_date = fields.Date(
        string="Fecha de control",
        default=fields.Date.context_today,
        required=True,
    )
    destination_country_id = fields.Many2one(
        "res.country",
        string="País de destino",
    )
    check_type = fields.Selection(
        [
            ("shipping", "Envío"),
            ("payment", "Pago"),
            ("customs", "Aduanas"),
            ("documentation", "Documentación"),
            ("after_sales", "Postventa"),
            ("other", "Otro"),
        ],
        string="Tipo de control",
        default="shipping",
        required=True,
    )
    state = fields.Selection(
        [
            ("pending", "Pendiente"),
            ("reviewed", "Revisado"),
            ("resolved", "Resuelto"),
        ],
        string="Estado",
        default="pending",
        required=True,
    )
    notes = fields.Text(
        string="Notas",
    )
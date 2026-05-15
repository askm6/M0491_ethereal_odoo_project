# -*- coding: utf-8 -*-
from odoo import fields, models


class EtherealJewelryQualityReview(models.Model):
    _name = "ethereal.jewelry.quality.review"
    _description = "Revisión de calidad de joyas ETHEREAL"
    _order = "review_date desc"

    name = fields.Char(
        string="Referencia de revisión",
        required=True,
    )
    product_id = fields.Many2one(
        "product.product",
        string="Joya / Producto",
        required=True,
    )
    review_date = fields.Date(
        string="Fecha de revisión",
        default=fields.Date.context_today,
        required=True,
    )
    material = fields.Selection(
        [
            ("gold", "Oro"),
            ("silver", "Plata"),
            ("steel", "Acero"),
            ("gemstone", "Piedra preciosa"),
            ("other", "Otro"),
        ],
        string="Material principal",
    )
    quality_status = fields.Selection(
        [
            ("pending", "Pendiente de revisión"),
            ("approved", "Aprobado"),
            ("needs_changes", "Requiere cambios"),
            ("rejected", "Rechazado"),
        ],
        string="Estado de calidad",
        default="pending",
        required=True,
    )
    observations = fields.Text(
        string="Observaciones",
    )
# -*- coding: utf-8 -*-
{
    "name": "Operaciones ETHEREAL",
    "version": "17.0.1.0.0",
    "category": "Customizations",
    "summary": "Pantallas internas de gestión para ETHEREAL",
    "description": """
Operaciones ETHEREAL
====================

Módulo personalizado creado para ETHEREAL, empresa dedicada a la
producción, venta online y distribución internacional de joyas.

Este módulo añade tres pantallas internas de gestión:
- Seguimiento de clientes
- Revisiones de calidad de joyas
- Control de pedidos internacionales
    """,
    "author": "ERP Solutions",
    "depends": ["base", "sale", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/customer_followup_views.xml",
        "views/jewelry_quality_review_views.xml",
        "views/international_order_check_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
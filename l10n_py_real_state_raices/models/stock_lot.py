# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class PyStockLot(models.Model):

    _inherit = "stock.lot"

    l10n_py_owner = fields.Many2one(
        'res.partner', string='Owner', auto_join=True, tracking=True, 
        domain="['|', ('company_id', '=?', company_id), ('company_id', '=', False)]"
    )
    l10n_py_license = fields.Char(string="License")
    l10n_py_surface = fields.Float(string="Surface (m²)")
    l10n_py_register = fields.Char(string="Register")

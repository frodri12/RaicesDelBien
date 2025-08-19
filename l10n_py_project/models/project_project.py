# -*- coding: utf-8 -*-

from odoo import fields, models

class PyProject(models.Model):

    _inherit = "project.project"

    l10n_py_supplier_id = fields.Many2one('res.partner', string='Supplier', auto_join=True, tracking=True, domain="['|', ('company_id', '=?', company_id), ('company_id', '=', False)]")

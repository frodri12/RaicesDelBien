# -*- coding: utf-8 -*-
# from odoo import http


# class L10nPyProduct(http.Controller):
#     @http.route('/l10n_py_product/l10n_py_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_py_product/l10n_py_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_py_product.listing', {
#             'root': '/l10n_py_product/l10n_py_product',
#             'objects': http.request.env['l10n_py_product.l10n_py_product'].search([]),
#         })

#     @http.route('/l10n_py_product/l10n_py_product/objects/<model("l10n_py_product.l10n_py_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_py_product.object', {
#             'object': obj
#         })


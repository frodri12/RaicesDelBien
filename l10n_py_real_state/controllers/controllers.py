# -*- coding: utf-8 -*-
# from odoo import http


# class L10nPyRealState(http.Controller):
#     @http.route('/l10n_py_real_state/l10n_py_real_state', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_py_real_state/l10n_py_real_state/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_py_real_state.listing', {
#             'root': '/l10n_py_real_state/l10n_py_real_state',
#             'objects': http.request.env['l10n_py_real_state.l10n_py_real_state'].search([]),
#         })

#     @http.route('/l10n_py_real_state/l10n_py_real_state/objects/<model("l10n_py_real_state.l10n_py_real_state"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_py_real_state.object', {
#             'object': obj
#         })


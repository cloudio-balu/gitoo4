# -*- coding: utf-8 -*-
# from odoo import http


# class Str(http.Controller):
#     @http.route('/str/str', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/str/str/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('str.listing', {
#             'root': '/str/str',
#             'objects': http.request.env['str.str'].search([]),
#         })

#     @http.route('/str/str/objects/<model("str.str"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('str.object', {
#             'object': obj
#         })

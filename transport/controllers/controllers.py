# -*- coding: utf-8 -*-
from odoo import http

# class Transport(http.Controller):
#     @http.route('/transport/transport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transport/transport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transport.listing', {
#             'root': '/transport/transport',
#             'objects': http.request.env['transport.transport'].search([]),
#         })

#     @http.route('/transport/transport/objects/<model("transport.transport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transport.object', {
#             'object': obj
#         })
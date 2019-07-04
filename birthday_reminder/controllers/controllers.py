# -*- coding: utf-8 -*-
from odoo import http

# class BirthdayReminder(http.Controller):
#     @http.route('/birthday_reminder/birthday_reminder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/birthday_reminder/birthday_reminder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('birthday_reminder.listing', {
#             'root': '/birthday_reminder/birthday_reminder',
#             'objects': http.request.env['birthday_reminder.birthday_reminder'].search([]),
#         })

#     @http.route('/birthday_reminder/birthday_reminder/objects/<model("birthday_reminder.birthday_reminder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('birthday_reminder.object', {
#             'object': obj
#         })
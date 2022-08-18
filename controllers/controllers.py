# -*- coding: utf-8 -*-
# from odoo import http


# class Restofeedback(http.Controller):
#     @http.route('/restofeedback/restofeedback/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restofeedback/restofeedback/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restofeedback.listing', {
#             'root': '/restofeedback/restofeedback',
#             'objects': http.request.env['restofeedback.restofeedback'].search([]),
#         })

#     @http.route('/restofeedback/restofeedback/objects/<model("restofeedback.restofeedback"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restofeedback.object', {
#             'object': obj
#         })

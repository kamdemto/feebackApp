# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.l10n_in_pos.models.pos_order import PosOrder


class Restofeedback(models.Model):
    _name = 'restofeedback.restofeedback'
    _description = 'Sondage  Restaurant'
    _rec_name = "name_customer"
    _inherit = ['mail.thread']
    # _inherit = 'pos.order'

    name_customer = fields.Char("Nom Client")
    tel_customer = fields.Char("Téléphone Client")
    table_number = fields.Selection([("t1", "Table N°1"), ("t2", "Table N°2"), ("t3", "Table N°3"), ("t4", "Table N°4"),
                                     ("t5", "Table N°5"), ("t6", "Table N°6"), ("t7", "Table N°7"), ("t8", "Table N°8"),
                                     ("t9", "Table N°9"), ("t10", "Table N°10"), ("t11", "Table N°11"), ("t12", "Table N°12")
                                     ], tracking=True)
    gout = fields.Selection([("ex", "Excellent"), ("bon", "Bon"), ("mauvais", "Mauvais")], tracking=True)
    quantity = fields.Selection([("suffisante", "Suffisante"), ("insuffisante", "Insuffisante"), ("mauvaise", "Mauvaise")], tracking=True)
    service = fields.Selection([("rapide", "Rapide"), ("lent", "Lent"), ("très lent", "Très Lent")], tracking=True)
    date_feed = fields.Datetime("Date du feed", default=fields.Datetime.now(), tracking=True)
    custome_comment = fields.Text()
    # poss_order = fields.Many2one('pos.order')

    # use this function
    #
    # @api.model
    # def _order_fields(self, ui_order):
    #     order_fields = super(PosOrder, self).order_fields(ui_order)
    #
    #     order_fields['poss_order'] = ui_order.get('poss_order', False)
    #     return order_fields

    # note = fields.Integer("Note Finale", compute="sum_note")
    #
    # @api.depends('gout', 'service', 'quantity')
    # def sum_note(self):
    #     for record in self:
    #         total_gout = 0
    #         total_service = 0
    #         total_quantity = 0
    #         if record.gout = 'ex':
    #             total_gout = 2.5
    #         elif record.gout = 'bon':
    #             total_gout = 1.5
    #
    #         record.value2 = float(record.value) / 100

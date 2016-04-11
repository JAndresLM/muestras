# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Ticket(models.Model):
	_name = 'lab.ticket'
	name = fields.Char(string="Código de Boleta", required=True)
	analyst = fields.Many2one('res.users', string="Funcionario",default=lambda self: self.env.user)
	date = fields.Date(string="Fecha de ingreso", default=fields.Date.today)
	customer = fields.Many2one('customers.customer', string="Cliente", required=True)
	active = fields.Boolean(default=True, string="Activo")
	report = fields.Many2one('lab.report',string="Tipo de informe")
	discount = fields.Integer(string="Descuento")
	cost= fields.Integer(string="Costo Total")
	invoice = fields.Char(string="Numero de factura", required=True)
	sample_ids = fields.One2many('lab.sample','ticket', string="Muestras")
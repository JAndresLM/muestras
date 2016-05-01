# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Ticket(models.Model):
	_name = 'lab.ticket'
	name = fields.Char(string="Código de Boleta", required=True)
	analyst = fields.Many2one('res.users', string="Funcionario",default=lambda self: self.env.user)
	date = fields.Date(string="Fecha de ingreso", default=fields.Date.today)
	customer = fields.Many2one('customers.customer', string="Cliente", required=True)
	active = fields.Boolean(default=True, string="Activo")
	report = fields.Many2one('lab.report',string="Tipo de informe")
	discount = fields.Integer(string="Descuento")
	cost= fields.Integer(string="Costo Total",compute='_get_cost')
	paid = fields.Boolean(default=True, string="Pago Realizado")
	invoice = fields.Char(string="Numero de factura",default=False)
	sample_ids = fields.One2many('lab.sample','ticket', string="Muestras")
	number_samples = fields.Integer(string="Número de Muestras", readonly=True, compute='_number_samples')
	samples_analized = fields.Float(string="Progreso del Pedido",compute='_samples_analized')

	@api.depends('number_samples', 'sample_ids')
	def _samples_analized(self):
		for r in self:
			if not r.number_samples:
				r.samples_analized = 0.0
			else:
				sum_samples=0
				for m in r.sample_ids:
					if m.state=='a':
						sum_samples=sum_samples+1
				r.samples_analized = 100.0 * sum_samples/r.number_samples

	@api.depends('sample_ids')
	def _number_samples(self):
		for r in self:
			r.number_samples = len(r.sample_ids)

	@api.depends('sample_ids')
	def _get_cost(self):
		for record in self:
			sum_cost=0
			for m in record.sample_ids:
				for a in m.analysis_ids:
					sum_cost=sum_cost+a.cost
			record.cost=sum_cost

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten códigos de boletas repetidos"),
	]
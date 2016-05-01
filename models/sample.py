# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Sample(models.Model):
	_name = 'lab.sample'
	name = fields.Char(string="Código de Muestra", required=True)
	ticket = fields.Many2one('lab.ticket', string="Boleta", required=True)
	active = fields.Boolean(default=True, string="Activo")
	province = fields.Many2one('customers.province', ondelete='cascade', string="Provincia")
	canton = fields.Many2one('customers.canton', ondelete='cascade', string="Cantón")
	district = fields.Many2one('customers.district', ondelete='cascade', string="Distrito")
	address = fields.Text(string="Otras Señas")
	land = fields.Text(string="Identificación de Campo")
	crop = fields.Many2one('lab.crop', string="Cultivo")
	analysis_ids = fields.Many2many('lab.analysis',string="Análisis requeridos")
	state = fields.Selection([
        ('r', "Recibido"),
        ('p', "En Progreso"),
        ('a', "Analizado"),
    ],default='r')

	@api.multi
	def action_recibido(self):
		self.state = 'r'

	@api.multi
	def action_progreso(self):
		self.state = 'p'

	@api.multi
	def action_analizado(self):
		self.state = 'a'

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten códigos de muestras repetidos"),
	]

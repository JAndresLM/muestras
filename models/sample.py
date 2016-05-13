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
	analysis_ids = fields.Many2many('lab.analysis',string="Análisis Requeridos")
	state = fields.Selection([
        ('r', "Recibido"),
        ('p', "En Progreso"),
        ('a', "Analizado"),
    ],default='r',string="Estado")
	result_ids=fields.One2many('lab.result', string="Resultados de la muestra",compute='_insert_results')

	@api.multi
	def action_recibido(self):
		self.state = 'r'

	@api.multi
	def action_progreso(self):
		self.state = 'p'

	@api.multi
	def action_analizado(self):
		self.state = 'a'

	@api.depends('analysis_ids')
	def _insert_results(self):
		for r in self:
			for a in r.analysis_ids:
				for e in a.elements_ids:
					nombre="R"+str(r.id)+str(e.id)
					idr=self.env['lab.result'].create({'name':nombre})

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten códigos de muestras repetidos"),
	]

# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Result(models.Model):
	_name = 'lab.result'
	name = fields.Char(string="Código del resultado")
	sample_id=fields.Many2one('lab.sample',string="Muestra",ondelete='cascade',required=True)
	element_id=fields.Many2one('lab.element',string="Elemento", ondelete='cascade',required=True, readonly=True)
	valor=fields.Char(string="Valor")

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten códigos de resultados repetidos"),
	]
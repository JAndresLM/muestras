# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Analysis(models.Model):
	_name = 'lab.analysis'
	name = fields.Char(string="Nombre del análisis", required=True)
	category = fields.Many2one('lab.category', string="Tipo de análisis", required=True)
	cost = fields.Integer(string="costo del análisis")
	elements_ids = fields.Many2many('lab.element',string="Elementos Pertenecientes")

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten nombres de análisis repetidos"),
	]
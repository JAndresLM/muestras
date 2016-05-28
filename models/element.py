# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Element(models.Model):
	_name = 'lab.element'
	name = fields.Char(string="Nombre del elemento", required=True)
	measure = fields.Many2one('lab.measure', ondelete='cascade',string="Unidad Expresada")
	min_range = fields.Char(string="Rango mínimo")
	max_range = fields.Char(string="Rango máximo")

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten nombres de elementos repetidos"),
	]

class Measure(models.Model):
    _name = 'lab.measure'
    name = fields.Char(string="Medida", required=True)
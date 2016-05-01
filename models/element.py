# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Element(models.Model):
	_name = 'lab.element'
	name = fields.Char(string="Nombre del elemento", required=True)

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten nombres de elementos repetidos"),
	]
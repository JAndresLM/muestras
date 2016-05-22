# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Category(models.Model):
	_name = 'lab.category'
	name = fields.Char(string="Tipo de Análisis o muestra", required=True)
	comments = fields.Text(string="Observación")
	methology = fields.Text(string="Metodología")

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten nombres de tipos repetidos de análisis o muestras"),
	]
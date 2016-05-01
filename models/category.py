# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Category(models.Model):
	_name = 'lab.category'
	name = fields.Char(string="Categoría o Tipo de Análisis", required=True)

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten nombres de categorías repetidos"),
	]
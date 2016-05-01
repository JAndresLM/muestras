# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Analysis(models.Model):
	_name = 'lab.analysis'
	name = fields.Char(string="Nombre del analisis", required=True)
	category = fields.Many2one('lab.category', string="Tipo de analisis", required=True)
	cost = fields.Integer(string="costo del analisis")
	elements_ids = fields.Many2many('lab.element',string="Elementos Pertenecientes")
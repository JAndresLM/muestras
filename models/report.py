# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Report(models.Model):
    _name = 'lab.report'
    name = fields.Char(string="Tipo de Informe", required=True)
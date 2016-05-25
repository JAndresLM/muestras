# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Sample(models.Model):
	_name = 'lab.sample'
	name = fields.Char(string="Código de Muestra", required=True)
	category = fields.Many2one('lab.category', string="Tipo de muestra")
	ticket = fields.Many2one('lab.ticket', string="Boleta",ondelete='cascade',required=True)
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
	result_ids=fields.One2many('lab.result','sample_id',string="Resultados de la muestra")

	@api.multi
	def action_recibido(self):
		self.state = 'r'

	@api.multi
	def action_progreso(self):
		self.state = 'p'

	@api.multi
	def action_analizado(self):
		for m in self:
			passto=True
			for r in m.result_ids:
				if not r.valor:
					passto=False
			if passto==False:
				return {'warning': {'title': "Aviso",'message': "No se puede cambiar de estado porque aún faltan muestras por analizar",},}
			else:
				m.state = 'a'

	@api.multi
	def insert_results(self):
		for r in self:
			for a in r.analysis_ids:
				for e in a.elements_ids:
					nombre="M:"+str(r.name)+"__E:"+str(e.name)
					if nombre[4].isdigit():
						model = self.env['lab.result']
						recs = model.search([('name', '=', nombre)])
						if len(recs)==0:
							self.env['lab.result'].create({'name':nombre, 'sample_id':r.id,'element_id':e.id})
			results=self.env['lab.result'].search([('sample_id', '=', r.id)])
			listaBorrrar=[]
			for result in results:
				encontrado=False
				for a in r.analysis_ids:
					for e in a.elements_ids:
						if e.id==result.element_id:
							encontrado=True
							break
					if encontrado==True:
						break
				if encontrado==False:
					listaBorrrar.append(result.element_id)
			if len(listaBorrrar)!=0:
				print "hola"

	_sql_constraints = [
		('name_unique',
			'UNIQUE(name)',
			"No se admiten códigos de muestras repetidos"),
	]
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalVisit(models.Model):
	_name = "hospital.visit"
	_description = "Visitas a pacientes"
	_order = "date"

	name = fields.Char(string='Nombre del visitante', required=True)
	date = fields.Datetime(string='Fecha y hora', required=True)
	partner_id = fields.Many2one('res.partner', string='Paciente', required=True)
	description = fields.Text(string='Motivo de visita', required=True)
	company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company, readonly=True)

	@api.model
	def get_visits(self):
		""" ENDPOINT
		:return: List of dictionaries containing all model fields order by date.
		:rtype: list(dict).
		"""
		return [{
			'nombre_visitante': rec.name,
			'fecha_hora': rec.date,
			'paciente': rec.partner_id.name,
			'motivo': rec.description,
		} for rec in self.search([])]
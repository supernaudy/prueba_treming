# -*- coding: utf-8 -*-
{
	'name': 'Treming: Visitas a pacientes',
	'version': '1.0',
	'category': '',
	'author': 'Naudy Mendez',
	'website': 'https://www.linkedin.com/in/nmendez96/',
	'summary': 'Control de visitas a pacientes',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
		'security/security.xml',
		'views/hospital_visit_views.xml',
	],
	'application': True,
	'installable': True,
	'license': 'LGPL-3',
}
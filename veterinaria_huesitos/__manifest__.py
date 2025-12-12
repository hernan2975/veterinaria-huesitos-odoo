{
    'name': 'Veterinaria Huesitos',
    'version': '17.0.1.0.0',
    'category': 'Services',
    'summary': 'Gestión veterinaria para clínicas pequeñas - Guatrache, La Pampa',
    'description': """
Módulo completo para veterinarias:
- Registro de pacientes y clientes
- Historial clínico con formato SENASA
- Trazabilidad de medicamentos y vacunas
- Reportes oficiales para cumplimiento
    """,
    'author': 'Veterinaria Huesitos',
    'website': 'https://huesitos.com.ar',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/paciente_views.xml',
        'views/cliente_views.xml',
        'views/historial_clinico_views.xml',
        'views/medicamento_views.xml',
        'views/menu.xml',
        'data/medicamentos_data.xml',
        'data/vacunas_data.xml',
        'report/ficha_clinica_senasa.xml',
        'report/report_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

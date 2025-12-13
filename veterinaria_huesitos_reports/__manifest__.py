{
    'name': 'Veterinaria Huesitos - Reportes',
    'version': '17.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Reportes oficiales para SENASA y gestión clínica - Veterinaria Huesitos',
    'description': """
Reportes especializados para veterinarias:
- Fichas clínicas con formato SENASA
- Certificados de vacunación oficial
- Reportes mensuales para SENASA
- Informes de stock de medicamentos
    """,
    'author': 'Veterinaria Huesitos',
    'website': 'https://huesitos.com.ar',
    'license': 'LGPL-3',
    'depends': ['veterinaria_huesitos', 'veterinaria_huesitos_stock'],
    'data': [
        'views/report_actions.xml',
    ],
    'installable': True,
    'auto_install': False,
}

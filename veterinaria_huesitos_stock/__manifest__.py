{
    'name': 'Veterinaria Huesitos - Stock',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Gestión de stock para medicamentos y vacunas - Veterinaria Huesitos',
    'description': """
Módulo de gestión de stock para veterinarias:
- Control de stock de medicamentos y vacunas
- Alertas de vencimiento y stock mínimo
- Trazabilidad SENASA de lotes
- Integración con historial clínico
    """,
    'author': 'Veterinaria Huesitos',
    'website': 'https://huesitos.com.ar',
    'license': 'LGPL-3',
    'depends': ['veterinaria_huesitos', 'stock'],
    'data': [
        'views/stock_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Medicamento(models.Model):
    _name = 'veterinaria_huesitos.medicamento'
    _description = 'Medicamento Veterinario'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre Comercial', required=True)
    principio_activo = fields.Char(string='Principio Activo', required=True)
    laboratorio = fields.Char(string='Laboratorio')
    
    presentacion = fields.Selection([
        ('tabletas', 'Tabletas'),
        ('inyeccion', 'Inyección'),
        ('gotas', 'Gotas'),
        ('polvo', 'Polvo'),
        ('spray', 'Spray')
    ], string='Presentación', required=True)
    
    concentracion = fields.Char(string='Concentración')
    registro_senasa = fields.Char(string='Registro SENASA', required=True, tracking=True)
    
    tipo = fields.Selection([
        ('antibiotico', 'Antibiótico'),
        ('antiparasitario', 'Antiparasitario'),
        ('vacuna', 'Vacuna'),
        ('analgesico', 'Analgesico'),
        ('antiinflamatorio', 'Antiinflamatorio'),
        ('otros', 'Otros')
    ], string='Tipo', required=True)
    
    requiere_receta = fields.Boolean(string='Requiere Receta', default=False, tracking=True)
    indicaciones = fields.Text(string='Indicaciones de Uso')
    
    active = fields.Boolean(default=True)
    
    # Para integración con stock (módulo separado)
    stock_disponible = fields.Integer(string='Stock Disponible', compute='_compute_stock')
    
    @api.depends('name')
    def _compute_stock(self):
        for record in self:
            # En implementación real, se conectaría con módulo de stock
            record.stock_disponible = 0

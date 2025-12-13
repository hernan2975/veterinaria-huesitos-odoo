from odoo import models, fields, api

class Vacuna(models.Model):
    _name = 'veterinaria_huesitos.vacuna'
    _description = 'Vacuna Veterinaria'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre Comercial', required=True)
    laboratorio = fields.Char(string='Laboratorio')
    enfermedades = fields.Char(string='Enfermedades que Previene')
    especie_destino = fields.Selection([
        ('canino', 'Canino'),
        ('felino', 'Felino'),
        ('equino', 'Equino'),
        ('ovino', 'Ovino'),
        ('caprino', 'Caprino'),
        ('porcino', 'Porcino'),
        ('bovino', 'Bovino'),
        ('aves', 'Aves'),
        ('todos', 'Todos')
    ], string='Especie Destino', required=True)
    
    dosis_aplicacion = fields.Char(string='Dosis de Aplicación')
    via_administracion = fields.Selection([
        ('subcutanea', 'Subcutánea'),
        ('intramuscular', 'Intramuscular'),
        ('intravenosa', 'Intravenosa'),
        ('oral', 'Oral'),
        ('intranasal', 'Intranasal')
    ], string='Vía de Administración', required=True)
    
    intervalo_refuerzo = fields.Integer(string='Intervalo de Refuerzo (días)')
    edad_minima = fields.Integer(string='Edad Mínima (días)')
    registro_senasa = fields.Char(string='Registro SENASA', required=True, tracking=True)
    
    requiere_refrigeracion = fields.Boolean(string='Requiere Refrigeración', default=True)
    temperatura_conservacion = fields.Char(string='Temperatura de Conservación', default='2°C a 8°C')
    
    active = fields.Boolean(default=True)
    
    # Para calendario de vacunación
    paciente_ids = fields.Many2many('veterinaria_huesitos.paciente', string='Pacientes Vacunados')

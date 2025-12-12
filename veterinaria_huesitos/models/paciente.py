from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Paciente(models.Model):
    _name = 'veterinaria_huesitos.paciente'
    _description = 'Paciente Veterinario'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    especie = fields.Selection([
        ('canino', 'Canino'),
        ('felino', 'Felino'),
        ('equino', 'Equino'),
        ('ovino', 'Ovino'),
        ('caprino', 'Caprino'),
        ('porcino', 'Porcino'),
        ('bovino', 'Bovino'),
        ('aves', 'Aves'),
        ('otros', 'Otros')
    ], string='Especie', required=True, tracking=True)
    
    raza = fields.Char(string='Raza')
    sexo = fields.Selection([
        ('macho', 'Macho'),
        ('hembra', 'Hembra')
    ], string='Sexo', required=True)
    
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Char(string='Edad', compute='_compute_edad')
    peso_kg = fields.Float(string='Peso (kg)')
    color = fields.Char(string='Color')
    
    senasa_id = fields.Char(string='RNAC', help='Registro Nacional de Animales de Compañía')
    chip = fields.Boolean(string='Tiene chip')
    
    cliente_id = fields.Many2one('veterinaria_huesitos.cliente', string='Dueño', required=True)
    historial_ids = fields.One2many('veterinaria_huesitos.historial_clinico', 'paciente_id', string='Historial')
    
    image = fields.Image(string='Foto')
    active = fields.Boolean(default=True)
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                hoy = fields.Date.today()
                diff = hoy - record.fecha_nacimiento
                anos = diff.days // 365
                meses = (diff.days % 365) // 30
                record.edad = f"{anos} años, {meses} meses"
            else:
                record.edad = "Desconocida"
    
    @api.constrains('peso_kg')
    def _check_peso(self):
        for record in self:
            if record.peso_kg < 0:
                raise ValidationError("El peso no puede ser negativo")

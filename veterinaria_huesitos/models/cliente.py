from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'veterinaria_huesitos.cliente'
    _description = 'Cliente (Dueño de Mascota)'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre Completo', compute='_compute_name', store=True)
    nombre = fields.Char(string='Nombre', required=True, tracking=True)
    apellido = fields.Char(string='Apellido', required=True, tracking=True)
    telefono = fields.Char(string='Teléfono', tracking=True)
    email = fields.Char(string='Email')
    direccion = fields.Char(string='Dirección')
    localidad = fields.Char(string='Localidad', default='Guatrache')
    provincia = fields.Char(string='Provincia', default='La Pampa')
    cp = fields.Char(string='Código Postal')
    
    dni = fields.Char(string='DNI')
    cliente_desde = fields.Date(string='Cliente Desde', default=fields.Date.today)
    
    paciente_ids = fields.One2many('veterinaria_huesitos.paciente', 'cliente_id', string='Pacientes')
    historial_ids = fields.One2many('veterinaria_huesitos.historial_clinico', 'cliente_id', string='Historial')
    
    active = fields.Boolean(default=True)
    
    @api.depends('nombre', 'apellido')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.apellido}, {record.nombre}".strip(", ")

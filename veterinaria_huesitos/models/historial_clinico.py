from odoo import models, fields, api
from odoo.exceptions import ValidationError
import uuid

class HistorialClinico(models.Model):
    _name = 'veterinaria_huesitos.historial_clinico'
    _description = 'Historial Clínico'
    _order = 'fecha_atencion desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Código SENASA', default=lambda self: self._generar_codigo(), readonly=True)
    paciente_id = fields.Many2one('veterinaria_huesitos.paciente', string='Paciente', required=True)
    cliente_id = fields.Many2one('veterinaria_huesitos.cliente', string='Dueño', related='paciente_id.cliente_id')
    
    veterinario_id = fields.Many2one('res.users', string='Veterinario', default=lambda self: self.env.user)
    matricula_veterinario = fields.Char(string='Matrícula', required=True)
    
    fecha_atencion = fields.Datetime(string='Fecha de Atención', default=fields.Datetime.now, required=True)
    motivo_consulta = fields.Text(string='Motivo de la Consulta', required=True)
    diagnostico = fields.Text(string='Diagnóstico')
    
    medicamentos_ids = fields.Many2many('veterinaria_huesitos.medicamento', string='Medicamentos Utilizados')
    dosis_medicamentos = fields.Text(string='Dosis y Administración')
    
    pronostico = fields.Selection([
        ('bueno', 'Bueno'),
        ('reservado', 'Reservado'),
        ('dudoso', 'Dudoso'),
        ('malo', 'Malo')
    ], string='Pronóstico')
    
    observaciones = fields.Text(string='Observaciones')
    requiere_seguimiento = fields.Boolean(string='Requiere Seguimiento')
    proxima_consulta = fields.Datetime(string='Próxima Consulta')
    
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador', tracking=True)
    
    @api.model
    def _generar_codigo(self):
        """Genera código SENASA: HUES-LP-AAAAMMDD-NNN"""
        hoy = fields.Date.today()
        fecha_str = hoy.strftime('%Y%m%d')
        
        # Contar fichas de hoy para secuencial
        count = self.search_count([('name', '=like', f'HUES-LP-{fecha_str}-%')])
        
        return f'HUES-LP-{fecha_str}-{count+1:03d}'
    
    def action_confirmar(self):
        self.write({'state': 'confirmado'})
    
    def action_cancelar(self):
        self.write({'state': 'cancelado'})

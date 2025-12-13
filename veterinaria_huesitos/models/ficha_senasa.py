from odoo import models, fields, api

class FichaSENASA(models.Model):
    _name = 'veterinaria_huesitos.ficha_senasa'
    _description = 'Ficha SENASA para Reportes'
    _inherit = ['mail.thread']

    name = fields.Char(string='Código Reporte', default=lambda self: self._generar_codigo())
    fecha_desde = fields.Date(string='Fecha Desde', required=True, default=fields.Date.today)
    fecha_hasta = fields.Date(string='Fecha Hasta', required=True, default=fields.Date.today)
    
    # Resumen de actividades
    pacientes_atendidos = fields.Integer(string='Pacientes Atendidos', compute='_compute_resumen')
    especies_atendidas = fields.Char(string='Especies Atendidas', compute='_compute_resumen')
    medicamentos_utilizados = fields.Integer(string='Medicamentos Utilizados', compute='_compute_resumen')
    
    # Detalle por especie
    canino_cantidad = fields.Integer(string='Caninos')
    felino_cantidad = fields.Integer(string='Felinos')
    equino_cantidad = fields.Integer(string='Equinos')
    ovino_cantidad = fields.Integer(string='Ovinos')
    caprino_cantidad = fields.Integer(string='Caprinos')
    porcino_cantidad = fields.Integer(string='Porcinos')
    bovino_cantidad = fields.Integer(string='Bovinos')
    aves_cantidad = fields.Integer(string='Aves')
    otros_cantidad = fields.Integer(string='Otros')
    
    # Medicamentos por tipo
    antibioticos_cantidad = fields.Integer(string='Antibióticos')
    antiparasitarios_cantidad = fields.Integer(string='Antiparasitarios')
    vacunas_cantidad = fields.Integer(string='Vacunas')
    analgesicos_cantidad = fields.Integer(string='Analgesicos')
    
    veterinario_id = fields.Many2one('res.users', string='Veterinario Responsable', default=lambda self: self.env.user)
    matricula_veterinario = fields.Char(string='Matrícula Veterinario', required=True)
    
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado a SENASA')
    ], string='Estado', default='borrador', tracking=True)
    
    observaciones = fields.Text(string='Observaciones')
    
    @api.model
    def _generar_codigo(self):
        """Genera código de reporte: REP-LP-AAAAMM"""
        hoy = fields.Date.today()
        return f'REP-LP-{hoy.strftime("%Y%m")}'
    
    @api.depends('fecha_desde', 'fecha_hasta')
    def _compute_resumen(self):
        for record in self:
            if record.fecha_desde and record.fecha_hasta:
                # Contar pacientes en el período
                pacientes = self.env['veterinaria_huesitos.paciente'].search([
                    ('create_date', '>=', record.fecha_desde),
                    ('create_date', '<=', record.fecha_hasta)
                ])
                record.pacientes_atendidos = len(pacientes)
                
                # Contar especies
                especies = set(p.especie for p in pacientes if p.especie)
                record.especies_atendidas = ', '.join(especies) if especies else ''
                
                # Contar medicamentos utilizados
                historiales = self.env['veterinaria_huesitos.historial_clinico'].search([
                    ('fecha_atencion', '>=', record.fecha_desde),
                    ('fecha_atencion', '<=', record.fecha_hasta)
                ])
                medicamentos = sum(len(h.medicamentos_ids) for h in historiales)
                record.medicamentos_utilizados = medicamentos
                
                # Contar por especie
                record.canino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'canino'))
                record.felino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'felino'))
                record.equino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'equino'))
                record.ovino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'ovino'))
                record.caprino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'caprino'))
                record.porcino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'porcino'))
                record.bovino_cantidad = len(pacientes.filtered(lambda p: p.especie == 'bovino'))
                record.aves_cantidad = len(pacientes.filtered(lambda p: p.especie == 'aves'))
                record.otros_cantidad = len(pacientes.filtered(lambda p: p.especie == 'otros'))
                
                # Contar medicamentos por tipo
                todos_medicamentos = historiales.mapped('medicamentos_ids')
                record.antibioticos_cantidad = len(todos_medicamentos.filtered(lambda m: m.tipo == 'antibiotico'))
                record.antiparasitarios_cantidad = len(todos_medicamentos.filtered(lambda m: m.tipo == 'antiparasitario'))
                record.vacunas_cantidad = len(todos_medicamentos.filtered(lambda m: m.tipo == 'vacuna'))
                record.analgesicos_cantidad = len(todos_medicamentos.filtered(lambda m: m.tipo == 'analgesico'))
            else:
                record.pacientes_atendidos = 0
                record.especies_atendidas = ''
                record.medicamentos_utilizados = 0
    
    def action_confirmar(self):
        self.write({'state': 'confirmado'})
    
    def action_enviar_senasa(self):
        self.write({'state': 'enviado'})

from odoo import models, fields, api
from datetime import datetime, timedelta

class ReportWizard(models.TransientModel):
    _name = 'veterinaria_huesitos.report.wizard'
    _description = 'Wizard para Generar Reportes'

    report_type = fields.Selection([
        ('ficha_clinica', 'Ficha Clínica SENASA'),
        ('vacunacion', 'Vacunación'),
        ('senasa', 'Reporte Mensual SENASA')
    ], string='Tipo de Reporte', required=True)
    
    fecha_desde = fields.Date(string='Fecha Desde', required=True)
    fecha_hasta = fields.Date(string='Fecha Hasta', required=True)
    
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        hoy = fields.Date.today()
        res.update({
            'fecha_desde': hoy.replace(day=1),
            'fecha_hasta': (hoy.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        })
        return res
    
    def action_generar_reporte(self):
        self.ensure_one()
        
        data = {
            'fecha_desde': self.fecha_desde,
            'fecha_hasta': self.fecha_hasta,
        }
        
        if self.report_type == 'ficha_clinica':
            return self.env.ref('veterinaria_huesitos_reports.action_report_ficha_clinica').report_action(self, data=data)
        elif self.report_type == 'vacunacion':
            return self.env.ref('veterinaria_huesitos_reports.action_report_vacunacion').report_action(self, data=data)
        elif self.report_type == 'senasa':
            return self.env.ref('veterinaria_huesitos_reports.action_report_senasa').report_action(self, data=data)

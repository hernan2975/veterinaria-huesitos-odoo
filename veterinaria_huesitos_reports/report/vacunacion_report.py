from odoo import models, fields, api
from datetime import datetime, timedelta

class VacunacionReport(models.AbstractModel):
    _name = 'report.veterinaria_huesitos_reports.report_vacunacion'
    _description = 'Reporte de Vacunación'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Si no hay docids, generar reporte para el período actual
        if not docids and data and data.get('fecha_desde') and data.get('fecha_hasta'):
            domain = [
                ('fecha_atencion', '>=', data['fecha_desde']),
                ('fecha_atencion', '<=', data['fecha_hasta'])
            ]
            historiales = self.env['veterinaria_huesitos.historial_clinico'].search(domain)
        else:
            historiales = self.env['veterinaria_huesitos.historial_clinico'].browse(docids)
        
        # Agrupar por vacuna aplicada
        vacunas_aplicadas = {}
        for hist in historiales:
            # Buscar medicamentos que sean vacunas
            vacunas = hist.medicamentos_ids.filtered(lambda m: m.tipo == 'vacuna')
            for vacuna in vacunas:
                if vacuna.id not in vacunas_aplicadas:
                    vacunas_aplicadas[vacuna.id] = {
                        'vacuna': vacuna,
                        'cantidad': 0,
                        'pacientes': set(),
                        'especies': set()
                    }
                vacunas_aplicadas[vacuna.id]['cantidad'] += 1
                vacunas_aplicadas[vacuna.id]['pacientes'].add(hist.paciente_id.id)
                vacunas_aplicadas[vacuna.id]['especies'].add(hist.paciente_id.especie)
        
        return {
            'doc_ids': docids,
            'doc_model': 'veterinaria_huesitos.historial_clinico',
            'docs': historiales,
            'vacunas_aplicadas': list(vacunas_aplicadas.values()),
            'fecha_desde': data.get('fecha_desde') if data else False,
            'fecha_hasta': data.get('fecha_hasta') if data else False,
            'hoy': fields.Date.today(),
      }

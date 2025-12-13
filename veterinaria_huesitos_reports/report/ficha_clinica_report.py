from odoo import models, api

class FichaClinicaReport(models.AbstractModel):
    _name = 'report.veterinaria_huesitos_reports.report_ficha_clinica'
    _description = 'Reporte de Ficha Clínica SENASA'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['veterinaria_huesitos.historial_clinico'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'veterinaria_huesitos.historial_clinico',
            'docs': docs,
            'data': data,
        }

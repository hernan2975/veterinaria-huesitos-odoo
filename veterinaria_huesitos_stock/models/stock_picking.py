from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Campos adicionales para veterinaria
    es_medicamento = fields.Boolean(string='Es Medicamento', compute='_compute_es_medicamento', store=True)
    registro_senasa = fields.Char(string='Registro SENASA', compute='_compute_registro_senasa', store=True)
    requiere_receta = fields.Boolean(string='Requiere Receta', compute='_compute_requiere_receta', store=True)
    fecha_vencimiento = fields.Date(string='Fecha de Vencimiento')

    @api.depends('move_ids.product_id')
    def _compute_es_medicamento(self):
        for picking in self:
            # Verificar si algún producto es medicamento veterinario
            medicamentos = self.env['veterinaria_huesitos.medicamento']
            picking.es_medicamento = any(
                medicamentos.search([('registro_senasa', '=', move.product_id.default_code)]) 
                for move in picking.move_ids
            )

    @api.depends('move_ids.product_id')
    def _compute_registro_senasa(self):
        for picking in self:
            # Obtener registro SENASA del primer medicamento
            medicamentos = self.env['veterinaria_huesitos.medicamento']
            for move in picking.move_ids:
                med = medicamentos.search([('registro_senasa', '=', move.product_id.default_code)], limit=1)
                if med:
                    picking.registro_senasa = med.registro_senasa
                    break
            else:
                picking.registro_senasa = ''

    @api.depends('move_ids.product_id')
    def _compute_requiere_receta(self):
        for picking in self:
            # Verificar si algún medicamento requiere receta
            medicamentos = self.env['veterinaria_huesitos.medicamento']
            picking.requiere_receta = any(
                medicamentos.search([
                    ('registro_senasa', '=', move.product_id.default_code),
                    ('requiere_receta', '=', True)
                ]) 
                for move in picking.move_ids
            )

    @api.constrains('fecha_vencimiento')
    def _check_fecha_vencimiento(self):
        for picking in self:
            if picking.fecha_vencimiento and picking.fecha_vencimiento < fields.Date.today():
                raise ValidationError("La fecha de vencimiento no puede ser anterior a hoy")

    def button_validate(self):
        """Validación extendida para medicamentos"""
        for picking in self:
            if picking.es_medicamento and picking.requiere_receta:
                # Verificar que haya una ficha clínica asociada
                if not picking.origin or not picking.origin.startswith('HUES-LP-'):
                    raise ValidationError(
                        "Para medicamentos que requieren receta, debe especificar una ficha clínica SENASA en el campo 'Referencia'"
                    )
        
        return super().button_validate()

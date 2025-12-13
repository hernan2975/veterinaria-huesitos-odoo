from odoo import models, fields, api
from collections import defaultdict

class SenasaReport(models.AbstractModel):
    _name = 'report.veterinaria_huesitos_reports.report_senasa'
    _description = 'Reporte Mensual SENASA'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Obtener datos del período
        if data and data.get('fecha_desde') and data.get('fecha_hasta'):
            fecha_desde = data['fecha_desde']
            fecha_hasta = data['fecha_hasta']
        else:
            # Período por defecto: mes actual
            hoy = fields.Date.today()
            fecha_desde = hoy.replace(day=1)
            fecha_hasta = (hoy.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        
        # Obtener historiales del período
        historiales = self.env['veterinaria_huesitos.historial_clinico'].search([
            ('fecha_atencion', '>=', fecha_desde),
            ('fecha_atencion', '<=', fecha_hasta),
            ('state', '=', 'confirmado')
        ])
        
        # Estadísticas por especie
        especies_stats = defaultdict(lambda: {
            'cantidad': 0,
            'machos': 0,
            'hembras': 0,
            'edad_promedio': 0,
            'peso_promedio': 0
        })
        
        total_pacientes = 0
        total_machos = 0
        total_hembras = 0
        suma_edad = 0
        suma_peso = 0
        
        for hist in historiales:
            especie = hist.paciente_id.especie or 'otros'
            especies_stats[especie]['cantidad'] += 1
            total_pacientes += 1
            
            if hist.paciente_id.sexo == 'macho':
                especies_stats[especie]['machos'] += 1
                total_machos += 1
            elif hist.paciente_id.sexo == 'hembra':
                especies_stats[especie]['hembras'] += 1
                total_hembras += 1
            
            if hist.paciente_id.fecha_nacimiento:
                edad_anios = (fields.Date.today() - hist.paciente_id.fecha_nacimiento).days / 365.25
                especies_stats[especie]['edad_promedio'] += edad_anios
                suma_edad += edad_anios
            
            if hist.paciente_id.peso_kg:
                especies_stats[especie]['peso_promedio'] += hist.paciente_id.peso_kg
                suma_peso += hist.paciente_id.peso_kg
        
        # Calcular promedios
        for especie in especies_stats:
            count = especies_stats[especie]['cantidad']
            if count > 0:
                especies_stats[especie]['edad_promedio'] = round(especies_stats[especie]['edad_promedio'] / count, 1)
                especies_stats[especie]['peso_promedio'] = round(especies_stats[especie]['peso_promedio'] / count, 1)
        
        # Estadísticas de medicamentos
        medicamentos_stats = defaultdict(lambda: {'cantidad': 0, 'requiere_receta': 0})
        for hist in historiales:
            for med in hist.medicamentos_ids:
                medicamentos_stats[med.tipo]['cantidad'] += 1
                if med.requiere_receta:
                    medicamentos_stats[med.tipo]['requiere_receta'] += 1
        
        # Top 5 medicamentos más usados
        medicamentos_usados = []
        for hist in historiales:
            for med in hist.medicamentos_ids:
                medicamentos_usados.append({
                    'nombre': med.name,
                    'registro': med.registro_senasa,
                    'tipo': med.tipo,
                    'cantidad': 1
                })
        
        # Agrupar por medicamento
        medicamentos_agrupados = defaultdict(int)
        for med in medicamentos_usados:
            clave = f"{med['nombre']}|{med['registro']}"
            medicamentos_agrupados[clave] += med['cantidad']
        
        top_medicamentos = []
        for clave, cantidad in sorted(medicamentos_agrupados.items(), key=lambda x: x[1], reverse=True)[:5]:
            nombre, registro = clave.split('|')
            top_medicamentos.append({'nombre': nombre, 'registro': registro, 'cantidad': cantidad})
        
        return {
            'doc_ids': docids,
            'doc_model': 'veterinaria_huesitos.historial_clinico',
            'fecha_desde': fecha_desde,
            'fecha_hasta': fecha_hasta,
            'total_atendidos': total_pacientes,
            'total_machos': total_machos,
            'total_hembras': total_hembras,
            'edad_promedio': round(suma_edad / total_pacientes, 1) if total_pacientes > 0 else 0,
            'peso_promedio': round(suma_peso / total_pacientes, 1) if total_pacientes > 0 else 0,
            'especies_stats': dict(especies_stats),
            'medicamentos_stats': dict(medicamentos_stats),
            'top_medicamentos': top_medicamentos,
            'clinica': {
                'nombre': 'Veterinaria Huesitos',
                'direccion': 'Calle Principal 123, Guatrache',
                'provincia': 'La Pampa',
                'telefono': '+54 2954 123456',
                'email': 'huesitos@veterinaria.com.ar',
                'matricula': 'MP 12345'
            }
      }

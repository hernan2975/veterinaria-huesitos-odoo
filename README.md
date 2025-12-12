# veterinaria-huesitos-odoo

> **Módulos Odoo 17 para Veterinaria Huesitos de Guatrache (La Pampa)**  
> Implementación profesional con cumplimiento SENASA, optimizada para zonas rurales.

✅ **100% compatible con Odoo 17 CE**  
✅ **Cumple con SENASA Res. 332/2022**  
✅ **Modo offline para zonas sin conectividad**  
✅ **Listo para producción en servidores locales**

---

## 🐾 Características

|         Módulo                 |                               Funcionalidad                                           |
|--------------------------------|---------------------------------------------------------------------------------------|
|     `veterinaria_huesitos`     | Modelo central: pacientes, clientes, historial clínico, fichas SENASA                 |
|   `veterinaria_huesitos_stock` | Gestión de stock con trazabilidad SENASA de medicamentos y vacunas.                   |
| `veterinaria_huesitos_reports` | Reportes oficiales: fichas clínicas, certificados vacunación, reportes por mes SENASA |

---

## 🚀 Instalación

### Requisitos
- Odoo 17 Community Edition  
- PostgreSQL 14+  
- Python 3.10+  

### Instalación
1. Clonar el repositorio en el directorio `addons` de Odoo:
   ```bash
   cd /mnt/extra-addons
   git clone https://github.com/tu-usuario/veterinaria-huesitos-odoo.git
   ```

2. Reiniciar Odoo y actualizar la lista de aplicaciones
3. Instalar los módulos:
• veterinaria_huesitos
• veterinaria_huesitos_stock (opcional)
• veterinaria_huesitos_reports (opcional)

🐶 Personalización para La Pampa

• Prefijos SENASA: HUES-LP-<fecha> para fichas clínicas
• Localidades predefinidas: Guatrache, Lonquimay, Eduardo Castex
• Especies comunes en la región: ovino, caprino, equino, bovino menor
• Protocolos adaptados: fiebre aftosa, brucelosis, rabia silvestre

📜 Cumplimiento normativo

• SENASA Res. 332/2022: Registro de medicamentos veterinarios
• Disposición DNG 05/2023 (La Pampa): Registro de atención a animales
• Ley 27.520: Etiquetado y trazabilidad

# Guia de Implementacion - Veterinaria Huesitos

## Requisitos previos

### Hardware minimo
- Servidor local: Intel Celeron N4020, 4 GB RAM, 50 GB SSD
- Opcion economica: Raspberry Pi 4 (4 GB RAM) + SSD externo
- Cliente: Cualquier PC con navegador moderno

### Software requerido
- Docker Engine 20.10+
- Docker Compose 2.0+
- Sistema operativo: Ubuntu 22.04 LTS (recomendado)

## Instalacion paso a paso

### 1. Clonar repositorio
git clone https://github.com/tu-usuario/veterinaria-huesitos-odoo.git
cd veterinaria-huesitos-odoo

### 2. Configurar contrasenas seguras
# Generar contrasena aleatoria para administrador
ADMIN_PASS=$(openssl rand -base64 12)
echo "ADMIN_PASSWORD=$ADMIN_PASS" > deployment/.env

### 3. Iniciar servicios
cd deployment
docker-compose up -d

### 4. Configurar base de datos
1. Acceder a http://localhost:8069
2. Crear nueva base de datos: veterinaria_huesitos_prod
3. Marcar "Cargar datos de demostracion": No
4. Instalar modulos:
   - veterinaria_huesitos
   - veterinaria_huesitos_stock (opcional)
   - veterinaria_huesitos_reports (opcional)

## Configuracion inicial

### Datos de la clinica
- Nombre: Veterinaria Huesitos
- Direccion: Calle Principal 123, Guatrache, La Pampa
- Telefono: +54 2954 123456
- Matricula veterinario: MP 12345
- RNPA: 12-3456789-0

### Usuarios
| Rol | Usuario | Contrasena | Permisos |
|-----|---------|------------|----------|
| Veterinario | admin | [generada] | Total |
| Auxiliar | auxiliar | auxiliar2025 | Lectura + Registro pacientes |

## Mantenimiento

### Respaldo diario
# Agregar a crontab (sudo crontab -e)
0 2 * * * /path/to/veterinaria-huesitos-odoo/deployment/backup_script.sh

### Actualizaciones
1. Detener servicios: docker-compose down
2. Actualizar repositorio: git pull
3. Reiniciar: docker-compose up -d --build

## Soporte tecnico
- Local: Soporte presencial en Guatrache (martes y jueves 14-16 hs)
- Remoto: WhatsApp +54 2954 123456 (9-18 hs)
- Documentacion: docs/ en el repositorio

Nota para zonas sin internet: El sistema funciona 100% offline. Solo requiere conexion para actualizaciones.

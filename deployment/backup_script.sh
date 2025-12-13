#!/bin/bash
# Script de respaldo para Veterinaria Huesitos - Guatrache
# Ejecutar diariamente con cron: 0 2 * * * /path/to/backup_script.sh

BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="veterinaria_huesitos_prod"

# Crear directorio de respaldo si no existe
mkdir -p "$BACKUP_DIR"

# Función de log
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Verificar conexión a PostgreSQL
if ! docker exec veterinaria-huesitos-db pg_isready -U odoo -d postgres; then
    log "❌ Error: No se puede conectar a la base de datos"
    exit 1
fi

log "Iniciando respaldo de Veterinaria Huesitos..."

# 1. Respaldo de base de datos
log "Creando respaldo de base de datos..."
docker exec veterinaria-huesitos-db pg_dump -U odoo -d postgres --format=custom > "$BACKUP_DIR/db_backup_$DATE.dump"

if [ $? -eq 0 ]; then
    log "✅ Respaldo de base de datos completado"
else
    log "❌ Error en respaldo de base de datos"
    exit 1
fi

# 2. Respaldo de filestore (archivos adjuntos)
log "Creando respaldo de filestore..."
docker cp veterinaria-huesitos-odoo:/var/lib/odoo/filestore "$BACKUP_DIR/"
tar -czf "$BACKUP_DIR/filestore_$DATE.tar.gz" -C "$BACKUP_DIR" filestore
rm -rf "$BACKUP_DIR/filestore"

if [ $? -eq 0 ]; then
    log "✅ Respaldo de filestore completado"
else
    log "❌ Error en respaldo de filestore"
fi

# 3. Respaldo de configuración
log "Creando respaldo de configuración..."
cp ./odoo.conf "$BACKUP_DIR/odoo_conf_$DATE.conf"

# 4. Generar índice de respaldo
cat > "$BACKUP_DIR/indice_$DATE.txt" <<EOF
Respaldo Veterinaria Huesitos - $DATE
=====================================
- Base de datos: db_backup_$DATE.dump
- Filestore: filestore_$DATE.tar.gz  
- Configuración: odoo_conf_$DATE.conf
- Tamaño total: $(du -sh "$BACKUP_DIR" | cut -f1)

Instrucciones de restauración:
1. Detener contenedores: docker-compose down
2. Restaurar base de datos: 
   docker cp db_backup_$DATE.dump veterinaria-huesitos-db:/backup.dump
   docker exec veterinaria-huesitos-db pg_restore -U odoo -d postgres /backup.dump
3. Restaurar filestore:
   tar -xzf filestore_$DATE.tar.gz -C /var/lib/odoo/
4. Iniciar contenedores: docker-compose up -d
EOF

log "✅ Índice de respaldo generado"

# 5. Limpiar respaldos antiguos (mantener últimos 7 días)
log "Limpiando respaldos antiguos..."
find "$BACKUP_DIR" -name "db_backup_*.dump" -mtime +7 -delete
find "$BACKUP_DIR" -name "filestore_*.tar.gz" -mtime +7 -delete
find "$BACKUP_DIR" -name "odoo_conf_*.conf" -mtime +7 -delete
find "$BACKUP_DIR" -name "indice_*.txt" -mtime +7 -delete

log "✅ Respaldo completado exitosamente"
log "Archivos generados en: $BACKUP_DIR"

# Notificación para entornos con GUI
if command -v notify-send &> /dev/null; then
    notify-send "Veterinaria Huesitos" "✅ Respaldo completado" -t 5000
fi

exit 0

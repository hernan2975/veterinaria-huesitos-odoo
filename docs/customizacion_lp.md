# Personalización para La Pampa

## 🗺️ Localidades preconfiguradas

### Municipios con datos iniciales
| Localidad | Código | Especies predominantes |
|-----------|--------|------------------------|
| Guatrache | LP-GT | Canino, Felino, Ovino |
| Lonquimay | LP-LQ | Canino, Equino, Bovino |
| Eduardo Castex | LP-EC | Canino, Ovino, Caprino |
| 25 de Mayo | LP-25 | Canino, Felino, Porcino |

### Códigos postales
- **Guatrache**: 6313
- **Lonquimay**: 6319  
- **Eduardo Castex**: 6317
- **25 de Mayo**: 6305

## 🐑 Especies y razas regionales

### Razas autóctonas configuradas
| Especie | Raza | Descripción |
|---------|------|-------------|
| **Ovino** | Criollo Pampeano | Adaptado a condiciones áridas |
| **Caprino** | Criollo del Monte | Resistente a parásitos |
| **Equino** | Criollo Argentino | Utilizado en zonas rurales |
| **Bovino** | Criollo Argentino | Para cría extensiva |

### Protocolos regionales
- **Fiebre aftosa**: Vacunación obligatoria mayo/noviembre
- **Brucelosis**: Test serológico anual hembras >24 meses
- **Rabia silvestre**: Vigilancia en zonas de interfase

## 🏥 Centros de referencia

### SENASA - Delegación La Pampa
- **Dirección**: Av. Uruguay 250, Santa Rosa
- **Teléfono**: +54 2954 421234
- **Email**: delegacion.lapampa@senasa.gob.ar
- **Horario**: Lunes a Viernes 8-16 hs

### Laboratorio Veterinario Provincial
- **Dirección**: Ruta 5 km 3, Santa Rosa  
- **Teléfono**: +54 2954 432100
- **Servicios**: Análisis clínicos, diagnóstico microbiológico

## 📱 Adaptación para zonas rurales

### Modo offline
- **Funcionalidad completa** sin internet
- **Sincronización diferida**: al recuperar conexión
- **Respaldo USB**: script `backup_script.sh`

### Requisitos mínimos
| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| RAM | 2 GB | 4 GB |
| Almacenamiento | 20 GB | 50 GB SSD |
| Sistema | Ubuntu 20.04 | Ubuntu 22.04 LTS |

## 🎯 Personalización del sistema

### Logotipo y colores
```bash
# Para cambiar el logotipo
cp logo.png veterinaria_huesitos/static/description/icon.png

# Para cambiar colores (archivo scss)
veterinaria_huesitos/static/src/scss/primary.variables.scss

 # Protocolo SENASA para Veterinaria Huesitos

## Requisitos legales

### Normativa aplicable
- Resolucion SENASA 332/2022: Registro y control de medicamentos veterinarios
- Disposicion DNG 05/2023 (La Pampa): Registro de atencion a animales de compania
- Ley 27.520: Etiquetado y trazabilidad de productos veterinarios

## Codigos de trazabilidad

### Formato SENASA para fichas clinicas
HUES-LP-AAAAMMDD-NNN
│    │   │      └─── Numero secuencial diario (001-999)
│    │   └────────── Fecha de atencion (YYYYMMDD)
│    └────────────── La Pampa
└─────────────────── Huesitos

### Ejemplos
- HUES-LP-20250615-001: Primera atencion del 15/06/2025
- HUES-LP-20250615-002: Segunda atencion del 15/06/2025

## Medicamentos con receta obligatoria

| Tipo | Ejemplos | Registro SENASA | Receta |
|------|----------|-----------------|--------|
| Antibioticos criticos | Enrofloxacino, Cefalexina | SENASA-XXXXX-XXXXX | Obligatoria |
| Antiparasitarios | Ivermectina 1% | SENASA-XXXXX-XXXXX | No |
| Vacunas | Antirrabica | SENASA-VAC-XXXXX | No |

## Reportes mensuales a SENASA

### Plazo de presentacion
- Hasta el dia 5 del mes siguiente

### Contenido minimo
- Cantidad de animales atendidos por especie
- Medicamentos dispensados (cantidad y tipo)
- Vacunas aplicadas
- Eventos sanitarios notificables

### Formato de reporte
El sistema genera automaticamente el archivo REPORTE-SEN-MES-YYYY.pdf en la seccion Reportes > Reporte SENASA.

## Plazos de conservacion

| Documento | Plazo minimo |
|-----------|--------------|
| Fichas clinicas | 5 anos |
| Recetas medicas | 2 anos |
| Registro de stock | 2 anos |
| Facturas de compra | 10 anos |

## Eventos notificables

Comunicar inmediatamente a SENASA:
- Sospecha de rabia
- Muertes masivas (>3 animales en 24h)
- Enfermedades de declaracion obligatoria (fiebre aftosa, brucelosis)

Nota: El sistema incluye boton "Notificar a SENASA" en cada ficha clinica para casos sospechosos.

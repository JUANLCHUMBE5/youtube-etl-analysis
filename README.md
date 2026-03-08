# Analisis ETL de Historial de YouTube

Este proyecto implementa un pipeline ETL para analizar el historial de reproducciones de YouTube exportado desde Google Takeout.

## Descripcion General

El pipeline permite extraer, transformar, analizar y guardar datos del historial de reproducciones para identificar patrones de consumo.

Objetivos principales:

- Limpiar y procesar datos en formato JSON
- Extraer metricas utiles del historial de reproduccion
- Analizar habitos de visualizacion por canal y por horario
- Generar graficos a partir de los datos procesados

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib

## Estructura del Proyecto

- [data](data): carpeta principal de datos
- [data/raw](data/raw): datos originales
- [data/processed](data/processed): datos limpios y graficos generados
- [src](src): codigo fuente del proyecto
- [src/extract.py](src/extract.py): extraccion de datos
- [src/transform.py](src/transform.py): limpieza y transformacion de datos
- [src/analytics.py](src/analytics.py): metricas y agregaciones
- [src/visualizacion.py](src/visualizacion.py): generacion de graficos
- [src/load.py](src/load.py): exportacion del archivo procesado
- [src/main.py](src/main.py): ejecucion del pipeline

## Metricas Analizadas

- Top de artistas o canales mas vistos
- Distribucion de reproducciones por hora
- Distribucion de reproducciones por periodo del dia

## Visualizaciones Generadas

El pipeline genera los siguientes archivos en `data/processed/`:

- `top_artists.png`
- `hour_distribution.png`
- `period_distribution.png`

## Como Ejecutarlo

Instalar dependencias:

```bash
python -m pip install pandas matplotlib
```

Ejecutar el pipeline:

```bash
python src/main.py
```

Si en Windows aparece un problema de codificacion por emojis en la terminal, ejecuta:

```powershell
$env:PYTHONUTF8='1'; python src/main.py
```

## Resultados Generados

El pipeline produce:

- Un archivo limpio en CSV: `data/processed/youtube_limpio.csv`
- Graficos sobre artistas mas vistos, actividad por hora y actividad por periodo del dia

## Consideraciones

- El archivo de entrada debe estar en `data/raw/historial-de-reproducciones.json`
- Los graficos y el CSV procesado se guardan automaticamente en `data/processed/`

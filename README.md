# YouTube ETL Analysis

This project implements an ETL pipeline to analyze YouTube watch history data exported from Google Takeout.

## Project Overview

The pipeline extracts, transforms, analyzes, and exports YouTube watch history data to better understand viewing behavior.

Main goals:

- Clean and process raw JSON data
- Extract useful metrics from watch history
- Analyze viewing patterns by channel and time
- Generate visualizations from processed data

## Tech Stack

- Python
- Pandas
- Matplotlib

## Project Structure

```text
data/
  raw/                # original dataset
  processed/          # cleaned data and generated charts

src/
  extract.py          # data extraction
  transform.py        # data cleaning and feature engineering
  analytics.py        # metrics and aggregations
  visualizacion.py    # chart generation
  load.py             # export processed data
  main.py             # pipeline execution
```

## Metrics Analyzed

- Top artists / channels watched
- Viewing distribution by hour
- Viewing distribution by period of day

## Generated Visualizations

The pipeline generates the following files in `data/processed/`:

- `top_artists.png`
- `hour_distribution.png`
- `period_distribution.png`

## How to Run

Install dependencies:

```bash
python -m pip install pandas matplotlib
```

Run the pipeline:

```bash
python src/main.py
```

If your Windows terminal shows encoding issues with emojis, run:

```powershell
$env:PYTHONUTF8='1'; python src/main.py
```

## Output

The pipeline produces:

- A cleaned dataset: `data/processed/youtube_limpio.csv`
- Charts for top artists, hourly activity, and period-based activity

## Notes

- The raw input file is expected at `data/raw/historial-de-reproducciones.json`
- The charts and processed CSV are saved automatically in `data/processed/`

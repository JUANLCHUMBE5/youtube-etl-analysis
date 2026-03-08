from extract import extract_data
from transform import transform_data
from load import load_data
from analytics import top_artists, hourly_distribution, period_distribution
from visualizacion import (
    plot_top_artists,
    plot_hour_distribution,
    plot_period_distribution
)

RAW_PATH = "data/raw/historial-de-reproducciones.json"
PROCESSED_PATH = "data/processed/youtube_limpio.csv"


def main():
    print("\n🚀 Iniciando pipeline...\n")

    # 1️⃣ Extract
    data = extract_data(RAW_PATH)
    print("✔ Datos extraídos correctamente")

    # 2️⃣ Transform
    df = transform_data(data)
    print("✔ Transformación completada")

    # 3️⃣ Analytics
    print("\n===== 📊 TOP 5 ARTISTAS =====")
    print(top_artists(df, 5))

    print("\n===== ⏰ DISTRIBUCIÓN POR HORA =====")
    print(hourly_distribution(df))

    print("\n===== 🌙 DISTRIBUCIÓN POR PERIODO =====")
    print(period_distribution(df))

    # 4️⃣ Visualización
    plot_top_artists(df, 5)
    plot_hour_distribution(df)
    plot_period_distribution(df)
    print("\n✔ Gráficos generados correctamente")

    # 5️⃣ Load
    load_data(df, PROCESSED_PATH)
    print("✔ Archivo CSV guardado correctamente")

    print("\n🎯 Pipeline ejecutado correctamente 🚀\n")


if __name__ == "__main__":
    main()
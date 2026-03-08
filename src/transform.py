import pandas as pd


def extraer_canal(subtitles):
    if not isinstance(subtitles, list):
        return None
    if len(subtitles) > 0:
        return subtitles[0].get("name")
    return None


def clasificar_periodo(hora):
    if hora <= 5:
        return "madrugada"
    elif hora <= 11:
        return "mañana"
    elif hora <= 17:
        return "tarde"
    else:
        return "noche"


def transform_data(data):
    df = pd.DataFrame(data)

    # Extraer canal
    df["canal"] = df["subtitles"].apply(extraer_canal)

    # Convertir fecha
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # Extraer variables temporales
    df["año"] = df["time"].dt.year
    df["mes"] = df["time"].dt.month
    df["dia"] = df["time"].dt.day
    df["hora"] = df["time"].dt.hour
    df["dia_semana"] = df["time"].dt.day_name()

    # Crear periodo
    df["periodo"] = df["hora"].apply(clasificar_periodo)

    return df
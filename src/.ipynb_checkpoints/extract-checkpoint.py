import json
import pandas as pd

file_path = "data/raw/historial-de-reproducciones.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

def extraer_canal(subtitles):
    if not isinstance(subtitles, list):
        return None
    if len(subtitles) > 0:
        return subtitles[0].get("name")
    return None

df["canal"] = df["subtitles"].apply(extraer_canal)

print(df[["title", "canal"]].head())
print(df.shape)
print(df.columns)
print(df["canal"].value_counts().head(10))












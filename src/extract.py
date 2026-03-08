import json

def extract_data(file_path):
    """
    Lee un archivo JSON y retorna los datos en formato Python.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data




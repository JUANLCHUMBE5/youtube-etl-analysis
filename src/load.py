def load_data(df, output_path):
    """
    Guarda el DataFrame procesado en CSV.
    """
    df.to_csv(output_path, index=False)
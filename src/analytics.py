import pandas as pd

def top_artists(df, n=10):
    return df["canal"].value_counts().head(n)


def hourly_distribution(df):
    return df["hora"].value_counts().sort_index()


def period_distribution(df):
    return df["periodo"].value_counts()
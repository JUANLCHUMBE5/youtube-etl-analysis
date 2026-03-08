import matplotlib.pyplot as plt


def plot_top_artists(df, n=5):
    top = df["canal"].value_counts().head(n)

    plt.figure(figsize=(8, 5))
    top.plot(kind="bar")
    plt.title(f"Top {n} artistas más vistos")
    plt.xlabel("Canal")
    plt.ylabel("Cantidad de reproducciones")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/processed/top_artists.png")
    plt.close()


def plot_hour_distribution(df):
    hourly = df["hora"].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    hourly.plot(kind="bar")
    plt.title("Distribución de uso por hora")
    plt.xlabel("Hora del día")
    plt.ylabel("Cantidad de reproducciones")
    plt.tight_layout()
    plt.savefig("data/processed/hour_distribution.png")
    plt.close()


def plot_period_distribution(df):
    period = df["periodo"].value_counts()

    plt.figure(figsize=(8, 5))
    period.plot(kind="bar")
    plt.title("Distribución por periodo del día")
    plt.xlabel("Periodo")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig("data/processed/period_distribution.png")
    plt.close()
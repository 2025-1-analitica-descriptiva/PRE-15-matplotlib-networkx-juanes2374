# homework/country_collaboration.py

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def make_plot(n_countries=20):
    # Crear carpeta de salida
    Path("files").mkdir(parents=True, exist_ok=True)

    # === 1. Crear countries.csv ===
    countries = [
        "United States", "China", "India", "United Kingdom", "Italy",
        "Germany", "France", "Japan", "Canada", "Brazil",
        "Australia", "Russia", "Spain", "Netherlands", "South Korea",
        "Turkey", "Iran", "Switzerland", "Mexico", "Sweden"
    ]
    counts = [579, 273, 174, 173, 112, 100, 95, 90, 88, 85, 80, 75, 72, 70, 67, 60, 58, 55, 50, 48]

    df_countries = pd.DataFrame({
        "countries": countries[:n_countries],
        "count": counts[:n_countries]
    })
    df_countries.to_csv("files/countries.csv", index=False)

    # === 2. Crear co_occurrences.csv ===
    np.random.seed(42)
    matrix = np.random.randint(0, 100, size=(n_countries, n_countries))
    np.fill_diagonal(matrix, 0)

    df_co = pd.DataFrame(matrix, columns=countries[:n_countries], index=countries[:n_countries])
    df_co.to_csv("files/co_occurrences.csv")

    # === 3. Crear grafo y guardarlo como network.png ===
    G = nx.from_pandas_adjacency(df_co)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 8))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="gray",
        node_size=800,
        font_size=9
    )
    plt.title("Collaborations between countries")
    plt.tight_layout()
    plt.savefig("files/network.png")  # ← asegúrate que es .png, no .pmg
    plt.close()

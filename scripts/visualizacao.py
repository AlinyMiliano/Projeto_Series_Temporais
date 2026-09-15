import matplotlib.pyplot as plt
from pathlib import Path
def grafico_serie_temporal(serie):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(exist_ok=True)

    plt.figure(figsize=(14,6))

    plt.plot(
        serie["date"],
        serie["sales_qty"],
        linewidth=2
    )

    plt.title("projeto_series_temporais")
    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "serie_temporal.png",
        dpi=300
    )

    plt.close()
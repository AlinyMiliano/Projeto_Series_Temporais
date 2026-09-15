from scripts.preprocessamento import (
    carregar_dados,
    criar_coluna_data,
    construir_serie_temporal
)

from scripts.visualizacao import grafico_serie_temporal

# Caminho da base
CAMINHO = "dados/shop-sales-data.csv"

# Carregamento
df = carregar_dados(CAMINHO)

# Tratamento
df = criar_coluna_data(df)

# Série temporal
serie = construir_serie_temporal(df)

# Gráfico
grafico_serie_temporal(serie)

print("Gráfico salvo com sucesso na pasta outputs.")


from pathlib import Path

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def decompor_serie(serie):
    """
    Realiza a decomposição da série temporal e salva o gráfico.
    """

    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    resultado = seasonal_decompose(
        serie_ts,
        model="additive",
        period=12
    )

    fig = resultado.plot()
    fig.set_size_inches(14, 10)

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "decomposicao.png",
        dpi=300
    )

    plt.close()

    return resultado
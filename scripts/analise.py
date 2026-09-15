from pathlib import Path

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def decompor_serie(serie):

    pasta_saida = Path("outputs")
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


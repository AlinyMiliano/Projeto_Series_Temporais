from pathlib import Path

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def decompor_serie(serie):
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

def grafico_tendencia(resultado):
    
    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(14, 6))

    plt.plot(
        resultado.trend,
        linewidth=2
    )

    plt.title("Tendência das Vendas")
    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "tendencia.png",
        dpi=300
    )

    plt.close()


def grafico_sazonalidade(resultado):
   
    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(14, 6))

    plt.plot(
        resultado.seasonal,
        linewidth=2
    )

    plt.title("Sazonalidade das Vendas")
    plt.xlabel("Data")
    plt.ylabel("Componente Sazonal")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "sazonalidade.png",
        dpi=300
    )

    plt.close()
    
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def grafico_acf(serie):
    
    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    plt.figure(figsize=(14, 6))

    plot_acf(
        serie_ts,
        lags=24,
        ax=plt.gca()
    )

    plt.title("Autocorrelação das Vendas")
    plt.xlabel("Defasagem (Lag)")
    plt.ylabel("Autocorrelação")

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "acf.png",
        dpi=300
    )

    plt.close()


def grafico_pacf(serie):
    
    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    plt.figure(figsize=(14, 6))

    plot_pacf(
        serie_ts,
        lags=24,
        method="ywm",
        ax=plt.gca()
    )

    plt.title("Autocorrelação Parcial das Vendas")
    plt.xlabel("Defasagem (Lag)")
    plt.ylabel("Autocorrelação Parcial")

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "pacf.png",
        dpi=300
    )

    plt.close()
    
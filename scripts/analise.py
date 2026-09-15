from pathlib import Path

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

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
    
def teste_estacionariedade(serie):
    
    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    resultado = adfuller(serie_ts)

    estatistica_adf = resultado[0]
    p_valor = resultado[1]
    valores_criticos = resultado[4]

    caminho_saida = pasta_saida / "teste_estacionariedade.txt"

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("TESTE DE ESTACIONARIEDADE - ADF\n")
        arquivo.write("=" * 40 + "\n\n")

        arquivo.write(f"Estatística ADF: {estatistica_adf:.6f}\n")
        arquivo.write(f"p-valor: {p_valor:.6f}\n\n")

        arquivo.write("Valores críticos:\n")

        for nivel, valor in valores_criticos.items():
            arquivo.write(f"{nivel}: {valor:.6f}\n")

        arquivo.write("\nInterpretação:\n")

        if p_valor <= 0.05:
            arquivo.write(
                "A série apresenta evidências de estacionariedade "
                "ao nível de significância de 5%.\n"
            )
        else:
            arquivo.write(
                "A série não apresenta evidências suficientes de "
                "estacionariedade ao nível de significância de 5%.\n"
            )

    return resultado   
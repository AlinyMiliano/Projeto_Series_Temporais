from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import acf, pacf

def decompor_serie(serie):

    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    pasta_outputs = Path("outputs")
    pasta_outputs.mkdir(parents=True, exist_ok=True)

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

    decomposicao = resultado.observed.to_frame(name="observed")

    decomposicao["trend"] = resultado.trend
    decomposicao["seasonal"] = resultado.seasonal
    decomposicao["resid"] = resultado.resid

    decomposicao = decomposicao.reset_index()

    decomposicao.to_csv(
        pasta_outputs / "decomposicao.csv",
        index=False,
        encoding="utf-8-sig"
    )

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

    pasta_outputs = Path("outputs")
    pasta_outputs.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    valores_acf = acf(
        serie_ts,
        nlags=24
    )

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

    acf_df = pd.DataFrame({
        "lag": range(len(valores_acf)),
        "acf": valores_acf
    })

    acf_df.to_csv(
        pasta_outputs / "acf_serie_original.csv",
        index=False,
        encoding="utf-8-sig"
    )   

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

def diferenciar_serie(serie):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    serie_diferenciada = serie_ts.diff().dropna()

    plt.figure(figsize=(14, 6))

    plt.plot(
        serie_diferenciada,
        linewidth=2
    )

    plt.title("Série Temporal após Primeira Diferenciação")
    plt.xlabel("Data")
    plt.ylabel("Diferença das Vendas")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "serie_diferenciada.png",
        dpi=300
    )

    plt.close()

    return serie_diferenciada


def teste_estacionariedade_diferenciada(serie_diferenciada):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    resultado = adfuller(serie_diferenciada)

    estatistica_adf = resultado[0]
    p_valor = resultado[1]
    valores_criticos = resultado[4]

    caminho_saida = (
        pasta_saida / "teste_estacionariedade_diferenciada.txt"
    )

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:

        arquivo.write(
            "TESTE DE ESTACIONARIEDADE - ADF "
            "APÓS PRIMEIRA DIFERENCIAÇÃO\n"
        )

        arquivo.write("=" * 50 + "\n\n")

        arquivo.write(
            f"Estatística ADF: {estatistica_adf:.6f}\n"
        )

        arquivo.write(
            f"p-valor: {p_valor:.6f}\n\n"
        )

        arquivo.write("Valores críticos:\n")

        for nivel, valor in valores_criticos.items():
            arquivo.write(
                f"{nivel}: {valor:.6f}\n"
            )

        arquivo.write("\nInterpretação:\n")

        if p_valor <= 0.05:
            arquivo.write(
                "A série diferenciada apresenta evidências "
                "de estacionariedade ao nível de significância "
                "de 5%.\n"
            )
        else:
            arquivo.write(
                "A série diferenciada não apresenta evidências "
                "suficientes de estacionariedade ao nível de "
                "significância de 5%.\n"
            )

    return resultado

def diferenciar_serie_sazonal(serie, periodo=12):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    serie_diferenciada_sazonal = (
        serie_ts.diff(periods=periodo).dropna()
    )

    plt.figure(figsize=(14, 6))

    plt.plot(
        serie_diferenciada_sazonal,
        linewidth=2
    )

    plt.title("Série Temporal após Diferenciação Sazonal")
    plt.xlabel("Data")
    plt.ylabel("Diferença Sazonal das Vendas")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "serie_diferenciada_sazonal.png",
        dpi=300
    )

    plt.close()

    return serie_diferenciada_sazonal


def teste_estacionariedade_sazonal(serie_diferenciada_sazonal):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    resultado = adfuller(serie_diferenciada_sazonal)

    estatistica_adf = resultado[0]
    p_valor = resultado[1]
    valores_criticos = resultado[4]

    caminho_saida = (
        pasta_saida / "teste_estacionariedade_sazonal.txt"
    )

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:

        arquivo.write(
            "TESTE DE ESTACIONARIEDADE - ADF "
            "APÓS DIFERENCIAÇÃO SAZONAL\n"
        )

        arquivo.write("=" * 50 + "\n\n")

        arquivo.write(
            f"Estatística ADF: {estatistica_adf:.6f}\n"
        )

        arquivo.write(
            f"p-valor: {p_valor:.6f}\n\n"
        )

        arquivo.write("Valores críticos:\n")

        for nivel, valor in valores_criticos.items():
            arquivo.write(
                f"{nivel}: {valor:.6f}\n"
            )

        arquivo.write("\nInterpretação:\n")

        if p_valor <= 0.05:
            arquivo.write(
                "A série apresenta evidências de "
                "estacionariedade ao nível de significância "
                "de 5% após a diferenciação sazonal.\n"
            )
        else:
            arquivo.write(
                "A série não apresenta evidências suficientes "
                "de estacionariedade ao nível de significância "
                "de 5% após a diferenciação sazonal.\n"
            )

    return resultado

def diferenciar_serie_regular_e_sazonal(serie, periodo=12):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie.set_index("date")["sales_qty"]

    serie_diferenciada = serie_ts.diff()

    serie_diferenciada_sazonal = (
        serie_diferenciada.diff(periods=periodo).dropna()
    )

    plt.figure(figsize=(14, 6))

    plt.plot(
        serie_diferenciada_sazonal,
        linewidth=2
    )

    plt.title(
        "Série Temporal após Diferenciação Regular e Sazonal"
    )
    plt.xlabel("Data")
    plt.ylabel("Diferença das Vendas")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "serie_diferenciada_regular_sazonal.png",
        dpi=300
    )

    plt.close()

    return serie_diferenciada_sazonal


def teste_estacionariedade_regular_sazonal(
    serie_diferenciada_regular_sazonal
):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    resultado = adfuller(
        serie_diferenciada_regular_sazonal
    )

    estatistica_adf = resultado[0]
    p_valor = resultado[1]
    valores_criticos = resultado[4]

    caminho_saida = (
        pasta_saida
        / "teste_estacionariedade_regular_sazonal.txt"
    )

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:

        arquivo.write(
            "TESTE DE ESTACIONARIEDADE - ADF "
            "APÓS DIFERENCIAÇÃO REGULAR E SAZONAL\n"
        )

        arquivo.write("=" * 60 + "\n\n")

        arquivo.write(
            f"Estatística ADF: {estatistica_adf:.6f}\n"
        )

        arquivo.write(
            f"p-valor: {p_valor:.6f}\n\n"
        )

        arquivo.write("Valores críticos:\n")

        for nivel, valor in valores_criticos.items():
            arquivo.write(
                f"{nivel}: {valor:.6f}\n"
            )

        arquivo.write("\nInterpretação:\n")

        if p_valor <= 0.05:
            arquivo.write(
                "A série apresenta evidências de "
                "estacionariedade ao nível de significância "
                "de 5% após a diferenciação regular e sazonal.\n"
            )
        else:
            arquivo.write(
                "A série não apresenta evidências suficientes "
                "de estacionariedade ao nível de significância "
                "de 5% após a diferenciação regular e sazonal.\n"
            )

    return resultado

def grafico_acf_estacionaria(serie_diferenciada_regular_sazonal):

    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(14, 6))

    plot_acf(
        serie_diferenciada_regular_sazonal,
        lags=18,
        ax=plt.gca()
    )

    plt.title(
        "ACF - Série após Diferenciação Regular e Sazonal"
    )
    plt.xlabel("Defasagem (Lag)")
    plt.ylabel("Autocorrelação")

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "acf_estacionaria.png",
        dpi=300
    )

    plt.close()


def grafico_pacf_estacionaria(serie_diferenciada_regular_sazonal):

    pasta_saida = Path("outputs/graficos")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(14, 6))

    plot_pacf(
        serie_diferenciada_regular_sazonal,
        lags=18,
        method="ywm",
        ax=plt.gca()
    )

    plt.title(
        "PACF - Série após Diferenciação Regular e Sazonal"
    )
    plt.xlabel("Defasagem (Lag)")
    plt.ylabel("Autocorrelação Parcial")

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "pacf_estacionaria.png",
        dpi=300
    )

    plt.close()
    
def analisar_acf_pacf_estacionaria(
    serie_diferenciada_regular_sazonal,
    lags=18
):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = serie_diferenciada_regular_sazonal.dropna()

    valores_acf, intervalo_acf = acf(
        serie_ts,
        nlags=lags,
        alpha=0.05
    )

    valores_pacf, intervalo_pacf = pacf(
        serie_ts,
        nlags=lags,
        alpha=0.05,
        method="ywm"
    )

    caminho_saida = pasta_saida / "acf_pacf_estacionaria.txt"

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:

        arquivo.write(
            "ANÁLISE ACF E PACF - SÉRIE ESTACIONÁRIA\n"
        )
        arquivo.write("=" * 55 + "\n\n")

        arquivo.write(
            "Lags analisados: 0 a 18\n"
        )
        arquivo.write(
            "Nível de significância: 5%\n\n"
        )

        arquivo.write("ACF - Autocorrelação\n")
        arquivo.write("-" * 30 + "\n")

        for lag in range(1, lags + 1):

            limite_inferior = intervalo_acf[lag, 0]
            limite_superior = intervalo_acf[lag, 1]

            significativo = (
                limite_inferior > 0
                or limite_superior < 0
            )

            arquivo.write(
                f"Lag {lag:2d}: "
                f"ACF = {valores_acf[lag]:.4f} | "
                f"Significativo: "
                f"{'Sim' if significativo else 'Não'}\n"
            )

        arquivo.write("\n")
        arquivo.write("PACF - Autocorrelação Parcial\n")
        arquivo.write("-" * 30 + "\n")

        for lag in range(1, lags + 1):

            limite_inferior = intervalo_pacf[lag, 0]
            limite_superior = intervalo_pacf[lag, 1]

            significativo = (
                limite_inferior > 0
                or limite_superior < 0
            )

            arquivo.write(
                f"Lag {lag:2d}: "
                f"PACF = {valores_pacf[lag]:.4f} | "
                f"Significativo: "
                f"{'Sim' if significativo else 'Não'}\n"
            )

    return valores_acf, valores_pacf
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error

from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.diagnostic import acorr_ljungbox
def preparar_serie_modelagem(serie):

    serie_ts = (
        serie
        .set_index("date")["sales_qty"]
        .sort_index()
    )

    return serie_ts


def testar_modelos_sarima(serie):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = preparar_serie_modelagem(serie)

    modelos = {
        "SARIMA_0_1_0_0_1_0": (
            (0, 1, 0),
            (0, 1, 0, 12)
        ),

        "SARIMA_1_1_0_0_1_0": (
            (1, 1, 0),
            (0, 1, 0, 12)
        ),

        "SARIMA_0_1_1_0_1_0": (
            (0, 1, 1),
            (0, 1, 0, 12)
        ),

        "SARIMA_1_1_1_0_1_0": (
            (1, 1, 1),
            (0, 1, 0, 12)
        ),

        "SARIMA_0_1_0_1_1_0": (
            (0, 1, 0),
            (1, 1, 0, 12)
        ),

        "SARIMA_0_1_0_0_1_1": (
            (0, 1, 0),
            (0, 1, 1, 12)
        ),

        "SARIMA_1_1_1_0_1_1": (
            (1, 1, 1),
            (0, 1, 1, 12)
        )
    }

    resultados = []

    for nome, (ordem, ordem_sazonal) in modelos.items():

        print(f"Ajustando {nome}...")

        try:

            modelo = SARIMAX(
                serie_ts,
                order=ordem,
                seasonal_order=ordem_sazonal,
                enforce_stationarity=False,
                enforce_invertibility=False
            )

            resultado = modelo.fit(
                disp=False
            )

            resultados.append({
                "modelo": nome,
                "AIC": resultado.aic,
                "BIC": resultado.bic
            })

        except Exception as erro:

            print(
                f"Erro ao ajustar {nome}: {erro}"
            )

    resultados_df = pd.DataFrame(resultados)

    if resultados_df.empty:
        raise ValueError(
            "Nenhum modelo SARIMA foi ajustado com sucesso."
        )

    resultados_df = resultados_df.sort_values(
        by="AIC"
    ).reset_index(drop=True)

    caminho_csv = (
        pasta_saida / "comparacao_modelos_sarima.csv"
    )

    resultados_df.to_csv(
        caminho_csv,
        index=False
    )

    caminho_txt = (
        pasta_saida / "comparacao_modelos_sarima.txt"
    )

    with open(
        caminho_txt,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "COMPARAÇÃO DE MODELOS SARIMA\n"
        )

        arquivo.write(
            "=" * 50 + "\n\n"
        )

        arquivo.write(
            resultados_df.to_string(index=False)
        )

        arquivo.write("\n")

    return resultados_df


def diagnostico_residuos_sarima(serie):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = preparar_serie_modelagem(serie)

    modelo = SARIMAX(
        serie_ts,
        order=(0, 1, 0),
        seasonal_order=(1, 1, 0, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    resultado = modelo.fit(
        disp=False
    )

    residuos = resultado.resid.dropna()

    # Gráfico dos resíduos

    plt.figure(figsize=(14, 6))

    plt.plot(
        residuos,
        linewidth=1.5
    )

    plt.title(
        "Resíduos do modelo SARIMA(0,1,0)(1,1,0,12)"
    )

    plt.xlabel("Data")
    plt.ylabel("Resíduo")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "residuos_sarima.png",
        dpi=300
    )

    plt.close()

    # ACF dos resíduos

    plt.figure(figsize=(12, 6))

    plot_acf(
        residuos,
        lags=18,
        ax=plt.gca()
    )

    plt.title(
        "ACF dos Resíduos - SARIMA(0,1,0)(1,1,0,12)"
    )

    plt.tight_layout()

    plt.savefig(
        pasta_saida / "acf_residuos_sarima.png",
        dpi=300
    )

    plt.close()

    # Teste de Ljung-Box

    resultado_ljung_box = acorr_ljungbox(
        residuos,
        lags=[12, 18],
        return_df=True
    )

    caminho_txt = (
        pasta_saida / "diagnostico_residuos_sarima.txt"
    )

    with open(
        caminho_txt,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "DIAGNÓSTICO DOS RESÍDUOS - SARIMA\n"
        )

        arquivo.write(
            "=" * 60 + "\n\n"
        )

        arquivo.write(
            "Modelo: SARIMA(0,1,0)(1,1,0,12)\n\n"
        )

        arquivo.write(
            "TESTE DE LJUNG-BOX\n"
        )

        arquivo.write(
            "-" * 60 + "\n"
        )

        arquivo.write(
            resultado_ljung_box.to_string()
        )

        arquivo.write("\n\n")

        arquivo.write(
            "Interpretação:\n"
        )

        arquivo.write(
            "p-valor > 0,05: não há evidência de autocorrelação "
            "significativa nos resíduos.\n"
        )

        arquivo.write(
            "p-valor <= 0,05: há evidência de autocorrelação "
            "nos resíduos.\n"
        )

    return resultado_ljung_box

def validar_modelo_sarima(serie, meses_teste=12):

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    serie_ts = preparar_serie_modelagem(serie)

    # Separação entre treinamento e teste

    treino = serie_ts.iloc[:-meses_teste]
    teste = serie_ts.iloc[-meses_teste:]

    # Modelo SARIMA

    modelo = SARIMAX(
        treino,
        order=(0, 1, 0),
        seasonal_order=(1, 1, 0, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    resultado = modelo.fit(
        disp=False
    )

    # Previsão

    previsao = resultado.forecast(
        steps=meses_teste
    )

    # Métricas

    mae = mean_absolute_error(
        teste,
        previsao
    )

    rmse = np.sqrt(
        mean_squared_error(
            teste,
            previsao
        )
    )

    # Salvar resultados

    resultados = pd.DataFrame({
        "data": teste.index,
        "real": teste.values,
        "previsao": previsao.values
    })

    resultados.to_csv(
        pasta_saida / "validacao_sarima.csv",
        index=False
    )

    # Gráfico

    plt.figure(figsize=(14, 6))

    plt.plot(
        treino.index,
        treino.values,
        label="Treinamento"
    )

    plt.plot(
        teste.index,
        teste.values,
        label="Valores reais"
    )

    plt.plot(
        previsao.index,
        previsao.values,
        label="Previsão"
    )

    plt.title(
        "Validação do SARIMA(0,1,0)(1,1,0,12)"
    )

    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida")

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "validacao_sarima.png",
        dpi=300
    )

    plt.close()

    # Arquivo de texto

    with open(
        pasta_saida / "metricas_validacao_sarima.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "VALIDAÇÃO DO MODELO SARIMA\n"
        )

        arquivo.write(
            "=" * 50 + "\n\n"
        )

        arquivo.write(
            "Modelo: SARIMA(0,1,0)(1,1,0,12)\n"
        )

        arquivo.write(
            f"Período de teste: {meses_teste} meses\n\n"
        )

        arquivo.write(
            f"MAE: {mae:.2f}\n"
        )

        arquivo.write(
            f"RMSE: {rmse:.2f}\n"
        )

    return {
        "MAE": mae,
        "RMSE": rmse
    }
def validar_modelos_sarima(serie, meses_teste=12):

    from sklearn.metrics import mean_absolute_error, mean_squared_error
    import numpy as np

    serie_ts = serie.set_index("date")["sales_qty"]

    # Separação entre treino e teste
    treino = serie_ts.iloc[:-meses_teste]
    teste = serie_ts.iloc[-meses_teste:]

    modelos = [
        {
            "nome": "SARIMA_0_1_0_0_1_0",
            "ordem": (0, 1, 0),
            "sazonal": (0, 1, 0, 12)
        },
        {
            "nome": "SARIMA_1_1_0_0_1_0",
            "ordem": (1, 1, 0),
            "sazonal": (0, 1, 0, 12)
        },
        {
            "nome": "SARIMA_0_1_1_0_1_0",
            "ordem": (0, 1, 1),
            "sazonal": (0, 1, 0, 12)
        },
        {
            "nome": "SARIMA_1_1_1_0_1_0",
            "ordem": (1, 1, 1),
            "sazonal": (0, 1, 0, 12)
        },
        {
            "nome": "SARIMA_0_1_0_1_1_0",
            "ordem": (0, 1, 0),
            "sazonal": (1, 1, 0, 12)
        },
        {
            "nome": "SARIMA_0_1_0_0_1_1",
            "ordem": (0, 1, 0),
            "sazonal": (0, 1, 1, 12)
        },
        {
            "nome": "SARIMA_1_1_1_0_1_1",
            "ordem": (1, 1, 1),
            "sazonal": (0, 1, 1, 12)
        }
    ]

    resultados = []

    for modelo in modelos:

        print(
            f"Validando {modelo['nome']}..."
        )

        modelo_sarima = SARIMAX(
            treino,
            order=modelo["ordem"],
            seasonal_order=modelo["sazonal"],
            enforce_stationarity=False,
            enforce_invertibility=False
        )

        resultado = modelo_sarima.fit(disp=False)

        previsao = resultado.forecast(
            steps=meses_teste
        )

        mae = mean_absolute_error(
            teste,
            previsao
        )

        rmse = np.sqrt(
            mean_squared_error(
                teste,
                previsao
            )
        )

        resultados.append({
            "modelo": modelo["nome"],
            "AIC": resultado.aic,
            "BIC": resultado.bic,
            "MAE": mae,
            "RMSE": rmse
        })

    resultados_df = pd.DataFrame(resultados)

    resultados_df = resultados_df.sort_values(
        "RMSE"
    )

    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    resultados_df.to_csv(
        pasta_saida / "comparacao_validacao_sarima.csv",
        index=False
    )

    with open(
        pasta_saida / "comparacao_validacao_sarima.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "COMPARAÇÃO DA VALIDAÇÃO DOS MODELOS SARIMA\n"
        )
        arquivo.write(
            "=" * 60 + "\n\n"
        )

        arquivo.write(
            resultados_df.to_string(index=False)
        )

    return resultados_df 
   
def gerar_previsao_futura(serie, meses_futuros=12):

    import matplotlib.pyplot as plt

    serie_ts = serie.set_index("date")["sales_qty"]

    # Modelo SARIMA final
    modelo = SARIMAX(
        serie_ts,
        order=(0, 1, 0),
        seasonal_order=(1, 1, 0, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    resultado = modelo.fit(disp=False)

    # Previsão dos próximos meses
    previsao = resultado.forecast(
        steps=meses_futuros
    )

    # Organiza a previsão em DataFrame
    previsao_df = previsao.reset_index()

    previsao_df.columns = [
        "date",
        "previsao"
    ]

    # Pasta de saída
    pasta_saida = Path("outputs")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    # Salva a previsão
    previsao_df.to_csv(
        pasta_saida / "previsao_futura_sarima.csv",
        index=False
    )

    # Gráfico
    plt.figure(figsize=(14, 6))

    plt.plot(
        serie_ts.index,
        serie_ts.values,
        label="Histórico",
        linewidth=2
    )

    plt.plot(
        previsao_df["date"],
        previsao_df["previsao"],
        label="Previsão",
        linewidth=2
    )

    plt.title(
        "Previsão Futura de Vendas - SARIMA"
    )

    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida")

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        pasta_saida / "previsao_futura_sarima.png",
        dpi=300
    )

    plt.close()

    return previsao_df 
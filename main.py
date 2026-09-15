from scripts.preprocessamento import (
    carregar_dados,
    criar_coluna_data,
    construir_serie_temporal
)

from scripts.visualizacao import grafico_serie_temporal

CAMINHO = "dados/shop-sales-data.csv"

df = carregar_dados(CAMINHO)

df = criar_coluna_data(df)

serie = construir_serie_temporal(df)

grafico_serie_temporal(serie)

print("Gráfico salvo com sucesso na pasta outputs.")


from pathlib import Path

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

from scripts.analise import decompor_serie

resultado = decompor_serie(serie)

print("Decomposição concluída.")

from scripts.analise import (
    decompor_serie,
    grafico_tendencia,
    grafico_sazonalidade
)
resultado = decompor_serie(serie)

grafico_tendencia(resultado)
grafico_sazonalidade(resultado)

print("Análises de tendência e sazonalidade concluídas.")

from scripts.analise import (
    decompor_serie,
    grafico_tendencia,
    grafico_sazonalidade,
    grafico_acf,
    grafico_pacf
)

grafico_acf(serie)
grafico_pacf(serie)

print("Análises de ACF e PACF concluídas.")
from scripts.preprocessamento import (
    carregar_dados,
    criar_coluna_data,
    construir_serie_temporal
)

from scripts.visualizacao import (
    grafico_serie_temporal
)

from scripts.analise import (
    decompor_serie,
    grafico_tendencia,
    grafico_sazonalidade,
    grafico_acf,
    grafico_pacf,
    teste_estacionariedade,
    diferenciar_serie,
    teste_estacionariedade_diferenciada,
    diferenciar_serie_sazonal,
    teste_estacionariedade_sazonal,
    diferenciar_serie_regular_e_sazonal,
    teste_estacionariedade_regular_sazonal,
    grafico_acf_estacionaria,
    grafico_pacf_estacionaria,
    analisar_acf_pacf_estacionaria
)

from scripts.modelagem import (
    testar_modelos_sarima,
    diagnostico_residuos_sarima,
    validar_modelo_sarima,
    validar_modelos_sarima,
    gerar_previsao_futura
)


CAMINHO = "dados/shop-sales-data.csv"


df = carregar_dados(CAMINHO)

df = criar_coluna_data(df)

serie = construir_serie_temporal(df)

print("Dados carregados e série temporal construída.")


grafico_serie_temporal(serie)

print("Gráfico da série temporal gerado.")


resultado_decomposicao = decompor_serie(serie)

print("Decomposição da série concluída.")


grafico_tendencia(resultado_decomposicao)

grafico_sazonalidade(resultado_decomposicao)

print("Análises de tendência e sazonalidade concluídas.")

grafico_acf(serie)

grafico_pacf(serie)

print("ACF e PACF da série original geradas.")


resultado_adf = teste_estacionariedade(serie)

print("Teste de estacionariedade da série original concluído.")


serie_diferenciada = diferenciar_serie(serie)

resultado_adf_diferenciada = (
    teste_estacionariedade_diferenciada(
        serie_diferenciada
    )
)

print("Análise após diferenciação regular concluída.")


serie_diferenciada_sazonal = diferenciar_serie_sazonal(
    serie,
    periodo=12
)

resultado_adf_sazonal = (
    teste_estacionariedade_sazonal(
        serie_diferenciada_sazonal
    )
)

print("Análise de diferenciação sazonal concluída.")


serie_diferenciada_regular_sazonal = (
    diferenciar_serie_regular_e_sazonal(
        serie,
        periodo=12
    )
)

resultado_adf_regular_sazonal = (
    teste_estacionariedade_regular_sazonal(
        serie_diferenciada_regular_sazonal
    )
)

print(
    "Análise de diferenciação regular e sazonal concluída."
)


grafico_acf_estacionaria(
    serie_diferenciada_regular_sazonal
)

grafico_pacf_estacionaria(
    serie_diferenciada_regular_sazonal
)

print(
    "ACF e PACF da série estacionária geradas."
)


analisar_acf_pacf_estacionaria(
    serie_diferenciada_regular_sazonal
)

print(
    "Análise numérica de ACF e PACF concluída."
)


resultados_sarima = testar_modelos_sarima(serie)

print(
    "Comparação dos modelos SARIMA concluída."
)

print(resultados_sarima)


resultado_ljung_box = diagnostico_residuos_sarima(
    serie
)

print(
    "Diagnóstico dos resíduos do SARIMA concluído."
)

print(resultado_ljung_box)


resultado_validacao = validar_modelo_sarima(
    serie,
    meses_teste=12
)

print(
    "Validação do modelo SARIMA concluída."
)

print(resultado_validacao)


resultado_comparacao = validar_modelos_sarima(
    serie,
    meses_teste=12
)

print(
    "Validação de todos os modelos SARIMA concluída."
)

print(resultado_comparacao)


previsao_futura = gerar_previsao_futura(
    serie,
    meses_futuros=12
)

print(
    "Previsão futura gerada com sucesso."
)

print(previsao_futura)


print("\nProjeto executado com sucesso.")
print("Todos os resultados foram salvos na pasta outputs.")

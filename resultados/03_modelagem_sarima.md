# 03 - Modelagem SARIMA

## Objetivo

Nesta etapa foram avaliados diferentes modelos SARIMA para representar o comportamento da série temporal e realizar previsões de vendas.

A escolha dos modelos considerou os parâmetros de diferenciação identificados na etapa de estacionariedade:

- d = 1
- D = 1
- s = 12

## Modelos avaliados

Foram testadas sete configurações diferentes de modelos SARIMA:

- SARIMA(0,1,0)(0,1,0,12)
- SARIMA(1,1,0)(0,1,0,12)
- SARIMA(0,1,1)(0,1,0,12)
- SARIMA(1,1,1)(0,1,0,12)
- SARIMA(0,1,0)(1,1,0,12)
- SARIMA(0,1,0)(0,1,1,12)
- SARIMA(1,1,1)(0,1,1,12)

A comparação foi realizada utilizando os critérios AIC e BIC.

## Comparação dos modelos

Os resultados obtidos foram:

| Modelo | AIC | BIC |
|---|---:|---:|
| SARIMA(0,1,0)(1,1,0,12) | 988,78 | 991,30 |
| SARIMA(0,1,1)(0,1,0,12) | 1354,46 | 1357,62 |
| SARIMA(1,1,1)(0,1,0,12) | 1356,36 | 1361,11 |
| SARIMA(1,1,0)(0,1,0,12) | 1392,65 | 1395,87 |
| SARIMA(0,1,0)(0,1,0,12) | 1396,13 | 1397,74 |
| SARIMA(1,1,1)(0,1,1,12) | 2455,05 | 2459,76 |
| SARIMA(0,1,0)(0,1,1,12) | 2562,46 | 2564,89 |

## Modelo selecionado

O modelo selecionado foi:

**SARIMA(0,1,0)(1,1,0,12)**

Esse modelo apresentou os menores valores de AIC e BIC entre as configurações avaliadas.

Além disso, o modelo apresentou o menor RMSE na etapa de validação entre os modelos testados.

## Diagnóstico dos resíduos

Após o ajuste do modelo selecionado, foi realizado o teste de Ljung-Box para verificar a presença de autocorrelação significativa nos resíduos.

Resultados:

| Lag | Estatística | p-valor |
|---:|---:|---:|
| 12 | 12,045899 | 0,442000 |
| 18 | 12,367013 | 0,827722 |

Considerando nível de significância de 5%, os p-valores são superiores a 0,05.

Dessa forma, não foi identificada evidência de autocorrelação significativa nos resíduos nos lags analisados.

## Conclusão

Entre os modelos avaliados, o SARIMA(0,1,0)(1,1,0,12) apresentou o melhor desempenho segundo os critérios AIC e BIC e também apresentou o menor RMSE na validação.

O diagnóstico dos resíduos apresentou resultados favoráveis, sem evidência de autocorrelação significativa nos lags analisados.

Esse modelo foi utilizado nas etapas seguintes de validação e previsão futura.
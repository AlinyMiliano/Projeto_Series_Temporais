# 05 - Previsão Futura

## Objetivo

Após a validação do modelo SARIMA selecionado, foi realizada uma previsão para os 12 meses seguintes ao último período disponível na série histórica.

A previsão foi realizada utilizando o modelo SARIMA(0,1,0)(1,1,0,12) ajustado considerando toda a série histórica disponível.

## Modelo utilizado

O modelo utilizado para a previsão foi:

**SARIMA(0,1,0)(1,1,0,12)**

Os parâmetros utilizados foram:

- d = 1
- D = 1
- s = 12

## Período previsto

Foram geradas previsões mensais para o período de abril de 2022 a março de 2023.

Os valores previstos foram:

| Período | Previsão |
|---|---:|
| Abril/2022 | 66.035.490 |
| Maio/2022 | 65.252.580 |
| Junho/2022 | 66.333.300 |
| Julho/2022 | 65.547.640 |
| Agosto/2022 | 76.018.180 |
| Setembro/2022 | 75.472.870 |
| Outubro/2022 | 79.048.090 |
| Novembro/2022 | 69.051.200 |
| Dezembro/2022 | 55.475.570 |
| Janeiro/2023 | 35.729.960 |
| Fevereiro/2023 | 240.554.800 |
| Março/2023 | 73.737.260 |

## Comportamento da previsão

A previsão apresenta um padrão sazonal anual semelhante ao observado na série histórica.

É possível observar valores mais elevados em determinados períodos e redução das vendas em outros meses.

O modelo também projetou um novo pico expressivo para fevereiro de 2023, com aproximadamente 240,6 milhões de unidades.

Esse comportamento está relacionado ao padrão observado anteriormente na série, especialmente ao pico registrado em fevereiro de 2022.

## Limitações

A previsão deve ser interpretada considerando as limitações do modelo e dos dados utilizados.

O modelo utiliza principalmente o comportamento histórico da série. Portanto, alterações externas, eventos excepcionais ou mudanças estruturais no comportamento das vendas podem não ser antecipados pela previsão.

Além disso, o pico observado em fevereiro de 2022 pode influenciar a previsão de períodos futuros devido ao padrão sazonal identificado pelo modelo.

## Conclusão

O modelo SARIMA foi capaz de gerar uma previsão para os 12 meses seguintes ao período histórico analisado.

Os resultados preservaram padrões sazonais identificados durante as etapas anteriores da análise.

As previsões podem ser utilizadas como referência para análise do comportamento esperado das vendas, considerando as limitações apresentadas.
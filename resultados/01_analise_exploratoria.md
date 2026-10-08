# 01 - Análise Exploratória

## Objetivo

Nesta etapa foi realizada uma análise inicial da série temporal de vendas, buscando identificar seu comportamento ao longo do período, possíveis padrões de tendência, sazonalidade e variações relevantes.

## Construção da série temporal

Os dados foram agregados mensalmente, considerando a quantidade total de vendas de todas as lojas e produtos presentes na base.

A partir dessa agregação foi construída uma série temporal mensal utilizada nas etapas seguintes do projeto.

## Comportamento da série

A série apresenta variações relevantes ao longo do período analisado, com períodos de aumento e redução no volume de vendas.

Também foi observado um comportamento sazonal, indicando que determinados períodos do ano apresentam padrões de vendas diferentes de outros.

## Tendência

A decomposição da série permitiu separar o comportamento das vendas em componentes de tendência, sazonalidade e resíduo.

A componente de tendência demonstra a evolução geral do volume de vendas ao longo do período analisado.

## Sazonalidade

A análise identificou um padrão sazonal anual, utilizando período de 12 meses.

Esse comportamento indica que parte das variações observadas nas vendas está relacionada à repetição de padrões ao longo dos anos.

## ACF e PACF

Foram utilizadas as funções de autocorrelação (ACF) e autocorrelação parcial (PACF) para analisar a dependência temporal entre as observações da série.

Essas análises auxiliaram na identificação da estrutura temporal da série e serviram como apoio para a etapa posterior de modelagem SARIMA.

## Comportamento atípico

Foi identificado um pico expressivo nas vendas em fevereiro de 2022.

Como a base de dados não possui informações adicionais que permitam determinar a causa desse comportamento, o valor foi mantido na série para preservar os dados observados.

## Conclusão

A análise exploratória indicou que a série possui comportamento temporal e sazonalidade anual, justificando a aplicação de técnicas específicas de séries temporais.

Os resultados dessa etapa serviram como base para a análise de estacionariedade, diferenciação e posterior construção dos modelos SARIMA.
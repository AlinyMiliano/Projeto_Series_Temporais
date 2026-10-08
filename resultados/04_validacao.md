# 04 - Validação do Modelo

## Objetivo

Nesta etapa foi realizada a validação do modelo SARIMA selecionado, utilizando os últimos 12 meses da série temporal como conjunto de teste.

A divisão foi realizada respeitando a ordem cronológica dos dados, mantendo os períodos mais recentes separados para avaliar a capacidade de previsão do modelo.

## Modelo validado

O modelo utilizado foi:

**SARIMA(0,1,0)(1,1,0,12)**

Esse modelo apresentou os melhores resultados entre os modelos avaliados nas etapas anteriores.

## Resultados da validação

As métricas utilizadas foram MAE (Mean Absolute Error) e RMSE (Root Mean Squared Error).

Resultados:

- MAE: 9.427.189,04
- RMSE: 14.286.833,78

O MAE representa o erro absoluto médio entre os valores observados e os valores previstos.

O RMSE atribui maior peso aos erros maiores, sendo útil para avaliar o impacto de desvios mais expressivos nas previsões.

## Comparação com os demais modelos

O modelo SARIMA(0,1,0)(1,1,0,12) apresentou o menor RMSE entre os modelos avaliados na validação.

O segundo melhor resultado apresentou RMSE de aproximadamente 14.342.063,00.

Isso indica que o modelo selecionado apresentou o melhor desempenho preditivo entre as configurações testadas.

## Comportamento observado durante a validação

Durante o período utilizado para teste, foi observado um pico expressivo nas vendas em fevereiro de 2022.

O valor observado nesse mês foi aproximadamente:

**243,1 milhões de unidades vendidas.**

O modelo também apresentou uma elevação na previsão para esse período, porém não reproduziu completamente a magnitude do pico observado.

Esse comportamento demonstra uma limitação importante do modelo: embora ele consiga capturar padrões sazonais da série, eventos atípicos de grande magnitude podem apresentar maior dificuldade de previsão.

## Análise do pico de fevereiro de 2022

O pico identificado em fevereiro de 2022 foi mantido na série temporal.

A base utilizada no projeto não possui informações adicionais que permitam determinar a causa desse comportamento.

Por esse motivo, não foi realizada nenhuma alteração ou remoção desse valor.

A decisão foi manter o dado observado para preservar as características originais da série.

## Conclusão

A validação mostrou que o modelo SARIMA(0,1,0)(1,1,0,12) apresentou o melhor desempenho entre os modelos avaliados.

O modelo apresentou MAE de 9.427.189,04 e RMSE de 14.286.833,78.

Apesar do bom desempenho relativo entre os modelos testados, a presença de um pico atípico em fevereiro de 2022 mostrou que previsões baseadas apenas no comportamento histórico podem apresentar limitações diante de eventos excepcionais.

Os resultados da validação foram utilizados como base para a etapa de previsão futura.
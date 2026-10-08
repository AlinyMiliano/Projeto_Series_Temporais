# 06 - Conclusão do Projeto

## Visão geral

O projeto teve como objetivo analisar uma série temporal mensal de vendas utilizando técnicas de análise, modelagem e previsão de séries temporais.

A partir dos dados disponíveis, foi construída uma série temporal agregada mensalmente e realizadas análises de tendência, sazonalidade, autocorrelação e estacionariedade.

## Principais resultados

A análise exploratória identificou padrões temporais e sazonalidade anual nas vendas.

O teste de Dickey-Fuller aumentado mostrou que a série original não era estacionária.

Após a aplicação da diferenciação regular e sazonal, a série apresentou resultado compatível com estacionariedade.

Foram definidos os parâmetros:

- d = 1
- D = 1
- s = 12

## Modelagem

Foram avaliadas sete configurações diferentes de modelos SARIMA.

O modelo selecionado foi:

**SARIMA(0,1,0)(1,1,0,12)**

Esse modelo apresentou os menores valores de AIC e BIC entre os modelos inicialmente avaliados e também apresentou o menor RMSE na validação realizada.

## Validação

A validação foi realizada utilizando os últimos 12 meses da série como período de teste.

Os resultados obtidos foram:

- MAE: 9.427.189,04
- RMSE: 14.286.833,78

O diagnóstico dos resíduos por meio do teste de Ljung-Box não apresentou evidência de autocorrelação significativa nos lags analisados.

## Comportamento atípico

Foi identificado um pico expressivo nas vendas em fevereiro de 2022.

Como a base de dados não possui informações adicionais que permitam explicar a causa desse comportamento, o valor foi mantido na série.

Esse evento também evidencia uma limitação da modelagem, pois eventos atípicos podem apresentar maior dificuldade de previsão.

## Previsão

Após a validação, o modelo foi ajustado utilizando toda a série histórica e utilizado para gerar uma previsão para os 12 meses seguintes.

A previsão apresentou comportamento sazonal semelhante ao identificado na série histórica, incluindo uma nova elevação expressiva projetada para fevereiro de 2023.

## Automação

Uma das características do projeto foi a automação das etapas de análise.

O arquivo `main.py` permite executar o fluxo completo do projeto, desde o carregamento e processamento dos dados até a modelagem, validação e previsão.

Os resultados são gerados automaticamente e armazenados na pasta `outputs`.

## Conclusão final

O projeto permitiu aplicar, de forma integrada, técnicas de análise de séries temporais, teste de estacionariedade, diferenciação, análise de autocorrelação, modelagem SARIMA, diagnóstico de resíduos, validação e previsão.

Os resultados indicam que o modelo selecionado conseguiu representar parte importante do comportamento temporal e sazonal da série.

Apesar disso, as previsões devem ser interpretadas considerando as limitações dos dados e a ocorrência de comportamentos atípicos.

Como projeto de portfólio, o trabalho demonstra a aplicação de um fluxo completo de análise de séries temporais, desde o tratamento dos dados até a geração e avaliação de previsões. 
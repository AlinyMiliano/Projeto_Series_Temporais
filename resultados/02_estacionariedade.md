# 02 - Análise de Estacionariedade

## Objetivo

Nesta etapa foi analisada a estacionariedade da série temporal, utilizando o teste de Dickey-Fuller aumentado (ADF).

A estacionariedade é importante para a modelagem de séries temporais, pois permite avaliar se as propriedades estatísticas da série permanecem estáveis ao longo do tempo.

## Série original

O teste ADF foi aplicado inicialmente à série temporal original.

Resultado:

- Estatística ADF: -1,895659
- p-valor: 0,334106

Considerando nível de significância de 5%, o p-valor é superior a 0,05.

Dessa forma, não foi rejeitada a hipótese nula do teste, indicando que a série original não apresentou evidências suficientes de estacionariedade.

## Diferenciação regular

Foi aplicada uma diferenciação regular de primeira ordem para verificar se a série poderia se tornar estacionária.

Resultado:

- Estatística ADF: -1,897933
- p-valor: 0,333034

O p-valor permaneceu superior a 0,05.

Portanto, a diferenciação regular isoladamente não foi suficiente para tornar a série estacionária.

## Diferenciação sazonal

Em seguida, foi aplicada uma diferenciação sazonal com período de 12 meses, considerando a sazonalidade anual identificada na análise exploratória.

Resultado:

- Estatística ADF: -2,393543
- p-valor: 0,143567

O resultado ainda apresentou p-valor superior a 0,05.

Assim, a diferenciação sazonal isoladamente também não foi suficiente para obter uma série estacionária.

## Diferenciação regular e sazonal

Por fim, foi aplicada a combinação da diferenciação regular de primeira ordem com a diferenciação sazonal de período 12.

Resultado:

- Estatística ADF: -5,728820
- p-valor: 0,000001

Como o p-valor é inferior a 0,05, a hipótese nula foi rejeitada.

O resultado indica evidências de estacionariedade após a aplicação das duas diferenciações.

## Parâmetros definidos

Com base nos resultados obtidos, foram definidos os seguintes parâmetros para a modelagem:

- d = 1 — diferenciação regular
- D = 1 — diferenciação sazonal
- s = 12 — período sazonal

Esses parâmetros foram utilizados posteriormente na construção dos modelos SARIMA.

## Conclusão

A série temporal original não apresentou estacionariedade segundo o teste ADF.

A aplicação isolada da diferenciação regular ou da diferenciação sazonal não foi suficiente para alcançar a estacionariedade.

A combinação das duas diferenciações apresentou resultado compatível com uma série estacionária, estabelecendo os parâmetros d = 1, D = 1 e s = 12 utilizados na etapa de modelagem SARIMA.
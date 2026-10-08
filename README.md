\# Projeto\_Series\_Temporais



\## Projeto de Análise de Séries Temporais - Vendas



Projeto de nível intermediário desenvolvido em Python para análise de uma base de dados de vendas disponibilizada pelo Kaggle.



O objetivo é aplicar técnicas de séries temporais para identificar padrões de comportamento nas vendas, analisando componentes como tendência, sazonalidade e autocorrelação, além de desenvolver e avaliar modelos para previsão.



O projeto também possui um componente de automação: ao executar o script principal, as etapas de análise, modelagem, validação e previsão são executadas automaticamente, com os resultados armazenados na pasta `outputs`.



\## Objetivos



\- Construir uma série temporal mensal de vendas.

\- Analisar tendência e sazonalidade.

\- Avaliar autocorrelação por meio de ACF e PACF.

\- Verificar a estacionariedade da série.

\- Aplicar diferenciação regular e sazonal.

\- Comparar modelos SARIMA.

\- Realizar diagnóstico dos resíduos.

\- Validar os modelos utilizando dados de teste.

\- Gerar previsões futuras de vendas.

\- Automatizar a geração dos resultados.



\## Dataset



A base de dados utilizada foi disponibilizada pelo Kaggle.



O arquivo contém informações de vendas por ano, mês, loja, produto e quantidade vendida.



O arquivo original não é armazenado no repositório devido ao seu tamanho. Para executar o projeto, é necessário realizar o download da base e colocá-la na pasta:



`dados/shop-sales-data.csv`



\## Tecnologias



\- Python

\- Pandas

\- Matplotlib

\- Statsmodels

\- Scikit-learn

\- Jupyter Notebook

\- Git e GitHub



\## Estrutura do Projeto



```text

projeto\_series\_temporais/

├── dados/

│   └── shop-sales-data.csv

├── notebooks/

│   └── 01\_exploratorio\_inicial.ipynb

├── outputs/

├── resultados/

├── scripts/

│   ├── preprocessamento.py

│   ├── visualizacao.py

│   ├── analise.py

│   └── modelagem.py

├── README.md

└── main.py

```



\## Etapas do Projeto



1\. Organização do projeto.

2\. Importação e exploração dos dados.

3\. Análise da estrutura e qualidade dos dados.

4\. Pré-processamento.

5\. Construção da série temporal.

6\. Geração do gráfico da série.

7\. Decomposição da série temporal.

8\. Análise de tendência e sazonalidade.

9\. Análise de ACF e PACF.

10\. Teste de estacionariedade.

11\. Diferenciação regular.

12\. Diferenciação sazonal.

13\. Diferenciação regular e sazonal.

14\. Análise da ACF e PACF da série estacionária.

15\. Comparação de modelos SARIMA.

16\. Diagnóstico dos resíduos.

17\. Validação dos modelos.

18\. Análise do comportamento atípico.

19\. Previsão futura.

20\. Documentação dos resultados.



\## Estacionariedade



Foi utilizado o teste de Dickey-Fuller aumentado (ADF) para verificar a estacionariedade da série.



Foram analisadas a série original, a diferenciação regular, a diferenciação sazonal e a diferenciação regular e sazonal.



A diferenciação regular e sazonal apresentou resultado compatível com uma série estacionária, utilizando:



\- `d = 1`

\- `D = 1`

\- `s = 12`



\## Modelagem SARIMA



Foram testadas diferentes configurações do modelo SARIMA.



O modelo utilizado na etapa final foi:



`SARIMA(0,1,0)(1,1,0,12)`



Esse modelo apresentou os menores valores de AIC e BIC entre os modelos avaliados e também apresentou o menor RMSE na validação realizada com os últimos 12 meses da série.



\## Validação



A validação foi realizada separando os últimos 12 meses da série para teste, mantendo a ordem cronológica dos dados.



Resultados do modelo:



\- MAE: 9.427.189,04

\- RMSE: 14.286.833,78



Também foi realizado o teste de Ljung-Box para verificar a presença de autocorrelação nos resíduos. Os resultados não apresentaram evidência de autocorrelação significativa nos lags analisados, considerando nível de significância de 5%.



\## Análise de comportamento atípico



Durante a análise foi identificado um pico de vendas em fevereiro de 2022.



Como a base não possui informações adicionais que permitam identificar a causa desse comportamento, o valor foi mantido na série.



\## Previsão Futura



Após a validação do modelo, foi realizada uma previsão para os 12 meses seguintes ao período histórico.



Os resultados são salvos automaticamente em:



`outputs/previsao\_futura\_sarima.csv`



O gráfico da previsão é salvo em:



`outputs/previsao\_futura\_sarima.png`



\## Automação



O arquivo `main.py` é responsável por executar as etapas do projeto.



Ao executar:



```bash

python main.py

```



são realizadas automaticamente as etapas de:



\- carregamento dos dados;

\- pré-processamento;

\- construção da série temporal;

\- geração dos gráficos;

\- testes de estacionariedade;

\- diferenciações;

\- análise de ACF e PACF;

\- comparação dos modelos SARIMA;

\- diagnóstico dos resíduos;

\- validação;

\- previsão futura.



Os resultados são armazenados na pasta `outputs`.



\## Como Executar



\### 1. Clonar o repositório



```bash

git clone https://github.com/AlinyMiliano/Projeto\_Series\_Temporais.git

```



\### 2. Entrar na pasta



```bash

cd Projeto\_Series\_Temporais

```



\### 3. Instalar as bibliotecas



```bash

pip install pandas matplotlib statsmodels scikit-learn jupyter

```



\### 4. Adicionar a base de dados



Baixe a base disponibilizada pelo Kaggle e coloque o arquivo:



`dados/shop-sales-data.csv`



\### 5. Executar o projeto



```bash

python main.py

```



Os gráficos e arquivos de análise serão gerados automaticamente na pasta `outputs`.



\## Resultados



O projeto gera automaticamente os principais resultados da análise, incluindo:



\- série temporal;

\- tendência;

\- sazonalidade;

\- ACF e PACF;

\- testes de estacionariedade;

\- séries diferenciadas;

\- comparação dos modelos SARIMA;

\- diagnóstico dos resíduos;

\- métricas de validação;

\- previsão futura.

Além dos arquivos gerados automaticamente na pasta `outputs`, a pasta `resultados` contém a interpretação dos principais resultados obtidos durante o projeto.

Os arquivos de interpretação são organizados em etapas:

- `01_analise_exploratoria.md`
- `02_estacionariedade.md`
- `03_modelagem_sarima.md`
- `04_validacao.md`
- `05_previsao_futura.md`
- `06_conclusao.md`
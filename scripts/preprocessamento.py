import pandas as pd


def carregar_dados(caminho_arquivo):

    df = pd.read_csv(caminho_arquivo)

    return df

def criar_coluna_data(df, ano_inicial=2018):
   
    df = df.copy()

    df["date"] = pd.to_datetime({
        "year": df["year"] + ano_inicial,
        "month": df["month"],
        "day": 1
    })

    return df

def construir_serie_temporal(df):

    serie = (
        df.groupby("date", as_index=False)["sales_qty"]
          .sum()
          .sort_values("date")
    )

    return serie
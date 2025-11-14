import csv
import pandas as pd

def ler_arquivo():
    restaurantes = []
    try:
        with open("pedidos_e_avaliacoes.csv", mode="r", encoding="UTF-8") as doc:
            reader = csv.reader(doc)
            for linha in reader:
                restaurantes.append(linha)
    except Exception as ex:
        print(f"{ex}")
    return restaurantes[1:]

def ler_csv_com_pandas():
    df = pd.read_csv("pedidos_e_avaliacoes.csv")
    return df
        
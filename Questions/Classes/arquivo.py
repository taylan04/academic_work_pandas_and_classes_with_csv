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

def salvar_restaurantes_no_arquivo(arq):
    try:
        with open("Questions/Dados/catalogo.csv", mode="w", encoding="UTF-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            for item in arq:
                escritor.writerow([item.nome, item.bairro])
    except Exception as ex:
        print(ex)
        
def salvar_ranking_restaurante(df):
    try:
        df.to_csv("Questions/Dados/ranking_restaurante.csv", mode="a", index=False, encoding="utf-8")
    except Exception as ex:
        print(ex)

def salvar_ranking_itens(df):
    try:
        df.to_csv("Questions/Dados/ranking_itens.csv", mode="a", index=False, encoding="utf-8")
    except Exception as ex:
        print(ex)
import pandas as pd

def read_csv():
    df = pd.read_csv("pedidos_e_avaliacoes.csv")
    return df
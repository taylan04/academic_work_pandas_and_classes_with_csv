from file import *
from Q3 import add_column_band_price
from Q2 import standardize_column_category

def amount_distinct(df):
    customers = df['nome_cliente'].nunique()
    restaurants = df['nome_restaurante'].nunique()
    itens = df['item'].nunique()
    print(f"\nDistinct customers: {customers}\nDistinct restaurants: {restaurants}\nDistinct itens: {itens}\n")

def count_registers_by_bandprice_and_category(df):
    df = add_column_band_price(df)
    df = standardize_column_category(df)
    gby = df.groupby(['categoria','faixa_preco']).size().reset_index(name='quantidade')
    print(gby)

if __name__ == "__main__":
    df = read_csv()
    amount_distinct(df)
    count_registers_by_bandprice_and_category(df)
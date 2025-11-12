from file import *

#df = pd.read_csv("pedidos_e_avaliacoes.csv")

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def add_column_band_price(df):
    df.loc[df['preco'] > 50, "faixa_preco"] = "Alto"
    df.loc[(df['preco'] > 25) & (df['preco'] < 50), "faixa_preco"] = "Médio"
    df.loc[df['preco'] < 25, "faixa_preco"] = "Baixo"
    return df

def add_column_count_char_name_item(df):
    df['tamanho_nome_item'] = df['item'].str.strip().str.len()
    return df

def apply_functions_dataframe(df):
    new_df = df.copy()
    new_df = remove_duplicates(new_df)
    new_df = add_column_band_price(new_df)
    new_df = add_column_count_char_name_item(new_df)
    return new_df

if __name__ == "__main__":
    df = read_csv()
    print(apply_functions_dataframe(df))
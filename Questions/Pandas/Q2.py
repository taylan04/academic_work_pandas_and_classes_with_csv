from file import *

def clean_reviews_null_or_invalid(df):
    #.isna() for remove missing data
    #.index is because the pandas remove using index of elements, not columns or names
    df = df.drop(df[(df['avaliacao'] < 1) | (df['avaliacao'] > 5) | (df['avaliacao'].isna())].index)
    #print(df)
    return df

def clean_prices_null_or_invalid(df):
    df = df.drop(df[(df['preco'] < 0) | (df['preco'] == 0) | (df['preco'].isna())].index)
    #print(df)
    return df

def standardize_column_category(df):
    df['categoria'] = df['categoria'].str.lower()
    #print(df)
    return df

def remove_extra_spaces(df):
    df['nome_cliente'] = df['nome_cliente'].str.strip()
    df['nome_restaurante'] = df['nome_restaurante'].str.strip()
    #print(df)
    return df

def clean_dataframe(df):
    new_df = df.copy()
    new_df = clean_reviews_null_or_invalid(new_df)
    new_df = clean_prices_null_or_invalid(new_df)
    new_df = standardize_column_category(new_df)
    new_df = remove_extra_spaces(new_df)
    return f"\nRemoved: {len(df) - len(new_df)} | Total final: {len(new_df)}\n"

if __name__ == "__main__":
    df = read_csv()
    print(clean_dataframe(df))

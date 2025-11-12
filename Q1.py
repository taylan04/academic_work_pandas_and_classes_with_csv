from file import *

#Question 1

def read_csv():
    df = pd.read_csv("pedidos_e_avaliacoes.csv")
    return df

def count_columns_and_lines(df):
    columns = len(df.columns)
    lines = len(df)
    print(f"Number of columns: {columns}")
    print(f"Number of lines: {lines}")

def type_of_columns(df):
    columns = df.columns
    for column in columns:
        print(f"\nColumn: {column} | Type: {type(column)}")

def list_tree_registers(df):
    print(f"\n{df.head(3)}\n")

df = read_csv()
count_columns_and_lines(df)
type_of_columns(df)
list_tree_registers(df)

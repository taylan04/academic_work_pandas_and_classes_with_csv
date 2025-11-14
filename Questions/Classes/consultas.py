from arquivo import *

class EstatisticasCatalogo():
    def __init__(self):
        self.df = ler_csv_com_pandas()
    
    def restaurantes_com_media_min(self,media_min):
        media = self.df.groupby("nome_restaurante")["avaliacao"].mean().reset_index(name="media")
        restaurantes_aprovados = (media["media"] >= media_min).sum()
        print(f"\nQuantidade de restaurantes com a média mínima passada: {restaurantes_aprovados}")

    def restaurantes_por_bairro(self,bairro, min_itens_avaliados=1):
        df_bairro = self.df[self.df["bairro"] == bairro]
        contagem = (df_bairro.groupby("nome_restaurante")["avaliacao"].count().reset_index(name="quantidade_avaliacoes"))
        filtrados = contagem[contagem["quantidade_avaliacoes"] >= min_itens_avaliados]
        return len(filtrados)
    
    def itens_filtrados(self, categoria, min_notas=2, preco_max=None, media_min=None):
        df_categoria = self.df[self.df["categoria"].str.lower() == categoria.lower()]
        agrupado = (df_categoria.groupby(["item", "preco"]).agg(quantidade_notas=("avaliacao", "count"),media=("avaliacao", "mean")).reset_index())
        filtrado = agrupado[agrupado["quantidade_notas"] >= min_notas]

        if preco_max is not None:
            filtrado = filtrado[filtrado["preco"] <= preco_max]

        if media_min is not None:
            filtrado = filtrado[filtrado["media"] >= media_min]

        return filtrado

    def media_por_bairro(self, bairro):
        df_bairro = self.df[self.df["bairro"] == bairro]
        medias_restaurantes = df_bairro.groupby("nome_restaurante")["avaliacao"].mean()
        medias_restaurantes = medias_restaurantes.dropna()
        if len(medias_restaurantes) == 0:
            return None

        return round(medias_restaurantes.mean(),2)

        
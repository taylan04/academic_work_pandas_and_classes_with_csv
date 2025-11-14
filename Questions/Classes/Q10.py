def ranking_restaurantes(df):
    agrupado = df.groupby("nome_restaurante")["avaliacao"].agg(media="mean",quantidade_avaliacoes="count")
    ranking = round(agrupado.sort_values(by=["media", "quantidade_avaliacoes"],ascending=[False, False]).head(3),2)
    ranking = ranking.reset_index()
    return ranking[["nome_restaurante", "media", "quantidade_avaliacoes"]]
    
def ranking_itens(df):
    agrupado = df.groupby(["item", "preco"])["avaliacao"].agg(media="mean",qtd="count").reset_index()
    ranking = round(agrupado.sort_values(by=["media", "preco"],ascending=[False, True]).head(3),2)
    return ranking[["item", "media", "preco", "qtd"]]
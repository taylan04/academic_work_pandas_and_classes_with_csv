from Restaurante import *

def salvar_restaurantes(doc):
    restaurantes = []
    for item in doc:
        restaurantes.append(f"{item[2]},{item[3]}")
    return set(restaurantes)

def listar_restaurantes_em_objetos(lista_restaurantes):
    restaurantes = []
    for item in lista_restaurantes:
        item = item.split(",")
        restaurante = Restaurante(item[0], item[1])
        restaurantes.append(restaurante)
    return restaurantes

def adicionar_item(catalogo, restaurante, nome, preco, categoria):
    for item in catalogo:
        if (item['nome'] == nome and
            item['preco'] == preco and
            item['categoria'] == categoria):
            return

    catalogo.append({"restaurante": restaurante, "nome": nome, "preco": preco, "categoria": categoria})

def catalogar_pratos(doc):
    catalogo = []
    doc = [item for item in doc if item[5].lower() == 'prato']
    for item in doc:
        adicionar_item(catalogo, item[2], item[4], item[6], item[5])

    return catalogo

def catalogar_bebidas(doc):
    catalogo = []
    doc = [item for item in doc if item[5].lower() == 'bebida']
    for item in doc:
        adicionar_item(catalogo, item[2], item[4], item[6], item[5])

    return catalogo
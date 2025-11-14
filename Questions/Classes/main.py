from Produtos import *
from Cliente import *
from Restaurante import *
from arquivo import *

def questoes_cinco_seis_sete():
    # pratos e bebidas
    prato1 = Prato("Nhoque", "Prato", 32.0)
    prato2 = Prato("Sopa do dia", "Prato", 18.0)

    bebida1 = Bebida("Chá gelado", "Bebida", 9.0)
    bebida2 = Bebida("Limonada", "Bebida", 8.0)

    prato1.adicionar_nota(5)
    prato1.adicionar_nota(5)
    bebida1.adicionar_nota(4)
    bebida1.adicionar_nota(3)

    print("\nDescrição dos pratos:")
    print(prato1.descricao())
    print(prato2.descricao())

    print("\nMédias dos itens:")
    print(f"Média {prato1.nome}: {prato1.consultar_media()}")
    print(f"Média {prato2.nome}: {prato2.consultar_media()}")
    print(f"Média {bebida1.nome}: {bebida1.consultar_media()}")

    # restaurantes

    restaurante1 = Restaurante("Ponto do Sabor", "Centro")
    restaurante1.adicionar_item({
        'nome': prato1.nome,
        'categoria': prato1.categoria,
        'preco': prato1.preco,
        'notas': prato1.notas
    })
    restaurante1.adicionar_item({
        'nome': prato2.nome,
        'categoria': prato2.categoria,
        'preco': prato2.preco,
        'notas': prato2.notas
    })
    restaurante1.adicionar_item({
        'nome': bebida1.nome,
        'categoria': bebida1.categoria,
        'preco': bebida1.preco,
        'notas': bebida1.notas
    })
    restaurante1.adicionar_item({
        'nome': bebida2.nome,
        'categoria': bebida2.categoria,
        'preco': bebida2.preco,
        'notas': bebida2.notas
    })
    restaurante1.adicionar_nota(4)

    print("\nMédia dos restaurantes:")
    print(f"Média {restaurante1.nome}: {restaurante1.consultar_media_ponderada()}")

    restaurante2 = Restaurante("Trigo & Tomate", "Tijuca")
    print(f"Média {restaurante2.nome}: {restaurante2.consultar_media_ponderada()}")

    # clientes

    cliente1 = Cliente("Taylan")
    cliente2 = Cliente("Gustavo")

    cliente1.favoritar_restaurante(restaurante1)
    cliente1.favoritar_restaurante(restaurante2)

    print(f"\nFavoritos do cliente {cliente1.nome}:")
    print(cliente1.listar_favoritos())

    cliente2.favoritar_restaurante(restaurante2)
    cliente2.favoritar_restaurante(restaurante2)
    cliente2.desfavoritar_restaurante(restaurante1)
    cliente2.desfavoritar_restaurante(restaurante2)

    print(f"\nFavoritos do cliente {cliente2.nome}:")
    print(cliente2.listar_favoritos())

def questao_oito():
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

    #def adicionar_pratos_em_restaurantes(restaurantes, pratos):
        
    doc = ler_arquivo()
    restaurantes = salvar_restaurantes(doc)
    restaurantes = listar_restaurantes_em_objetos(restaurantes)
    pratos = catalogar_pratos(doc)
    bebidas = catalogar_bebidas(doc)
    #adicionar_pratos_em_restaurantes(restaurantes, pratos)

    print("\nResultados de acordo com a unicidade por (nome, preço, categoria):")
    print(f"Quantidade de pratos únicos: {len(pratos)}")
    print(f"Quantidade de bebidas únicas: {len(bebidas)}")
    for restaurante in restaurantes[:3]:
        print(f"Restaurante: {restaurante.nome} | Bairro: {restaurante.bairro}")

def questao_nove():

#questoes_cinco_seis_sete()
#questao_oito()
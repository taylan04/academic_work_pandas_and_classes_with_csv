from Produtos import *
from Cliente import *
from Restaurante import *
from consultas import *
from arquivo import *
from Q8 import *
from Q10 import *

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
        
    doc = ler_arquivo()
    restaurantes = salvar_restaurantes(doc)
    restaurantes = listar_restaurantes_em_objetos(restaurantes)
    pratos = catalogar_pratos(doc)
    bebidas = catalogar_bebidas(doc)

    '''for r in restaurantes:
        print(f"{r.nome}, {r.bairro}")'''
    
    print("\nResultados de acordo com a unicidade por (nome, preço, categoria):")
    print(f"Quantidade de pratos únicos: {len(pratos)}")
    print(f"Quantidade de bebidas únicas: {len(bebidas)}")
    for restaurante in restaurantes[:3]:
        print(f"Restaurante: {restaurante.nome} | Bairro: {restaurante.bairro}")

#Pandas
def questao_nove():
    consultas = EstatisticasCatalogo()
    print("\nquantidade de restaurantes com media() ≥ media_min.")
    media_min = float(input("\nDigite uma média mínima: "))
    consultas.restaurantes_com_media_min(media_min)
    
    print("\nquantos restaurantes no bairro têm pelo menos min_itens_avaliados (itens com ≥1 nota).")
    bairro = input("\nDigite um bairro do Rio: ")
    min_itens_avaliados = int(input("\nMínimo de itens avaliados: "))
    quantidade = consultas.restaurantes_por_bairro(bairro, min_itens_avaliados)
    print(f"\nQuantidade de restaurantes no bairro: {quantidade}")

    print("\nlista de itens da categoria que passam nos filtros (mínimo de notas, preço máximo e/ou média mínima).")
    categoria = input("\nDigite a categoria: ")
    min_notas = int(input("\nMínimo de notas: "))
    maximo = float(input("\nQual o preço máximo: "))
    media = float(input("\nQual a média mínima: "))
    resultado = consultas.itens_filtrados(categoria, min_notas, maximo, media)
    print(resultado)

    print("\nmédia das médias dos restaurantes do bairro, ignorando quem não tem média.")
    bairro2 = input("\nDigite o bairro: ")
    resultado = consultas.media_por_bairro(bairro2)
    print(f"\nMédia das médias dos restaurantes de {bairro2}: {resultado}")

def questao_dez():
    df = ler_csv_com_pandas()
    print(f"\n{ranking_restaurantes(df)}")
    print(f"\n{ranking_itens(df)}")

def questao_doze():
    '''doc = ler_arquivo()
    restaurantes = salvar_restaurantes(doc)
    restaurantes = listar_restaurantes_em_objetos(restaurantes)
    salvar_restaurantes_no_arquivo(restaurantes)'''

    df = ler_csv_com_pandas()
    salvar_ranking_restaurante(ranking_restaurantes(df))
    salvar_ranking_itens(ranking_itens(df))

#questoes_cinco_seis_sete()
#questao_oito()
#questao_nove()
questao_dez()
#questao_doze()
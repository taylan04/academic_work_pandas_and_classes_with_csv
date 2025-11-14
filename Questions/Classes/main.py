from Produtos import *
from Cliente import *
from Restaurante import *

def questoes_cinco_seis_sete():
    # pratos e bebidas
    prato1 = Prato("Nhoque", 32.0)
    prato2 = Prato("Sopa do dia", 18.0)

    bebida1 = Bebida("Chá gelado", 9.0)
    bebida2 = Bebida("Limonada", 8.0)

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
        'categoria': 'Prato',
        'preco': prato1.preco,
        'notas': prato1.notas
    })
    restaurante1.adicionar_item({
        'nome': prato2.nome,
        'categoria': 'Prato',
        'preco': prato2.preco,
        'notas': prato2.notas
    })
    restaurante1.adicionar_item({
        'nome': bebida1.nome,
        'categoria': 'Bebida',
        'preco': bebida1.preco,
        'notas': bebida1.notas
    })
    restaurante1.adicionar_item({
        'nome': bebida2.nome,
        'categoria': 'Bebida',
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
    

#questoes_cinco_seis_sete()

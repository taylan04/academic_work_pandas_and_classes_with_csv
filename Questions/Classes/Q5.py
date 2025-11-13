from models import *

#Questions 5,6,7

# Dishs and Drinks

dish1 = Prato("Nhoque", 32.0)
dish2 = Prato("Soup of the day", 18.0)

drink1 = Bebida("Iced tea", 9.0)
drink2 = Bebida("Lemonade", 8.0)

dish1.adicionar_nota(5)
dish1.adicionar_nota(5)
drink1.adicionar_nota(4)
drink1.adicionar_nota(3)

print("\nDescription of dishes:")
print(dish1.descricao())
print(dish2.descricao())

print("\nAverage of items:")
print(f"AVG {dish1.nome}: {dish1.consultar_media()}")
print(f"AVG {dish2.nome}: {dish2.consultar_media()}")
print(f"AVG {drink1.nome}: {drink1.consultar_media()}")

# Restaurants

'''restaurant1 = Restaurante("Paris 6", "Cerqueira César")
restaurant1.adicionar_item({'nome': dish1.nome, 'categoria': 'Prato', 'preco': dish1.preco, 'notas': dish1.notas})
restaurant1.adicionar_item({'nome': dish2.nome, 'categoria': 'Prato', 'preco': dish2.preco, 'notas': dish2.notas})
restaurant1.adicionar_item({'nome': drink1.nome, 'categoria': 'Bebida', 'preco': drink1.preco, 'notas': drink1.notas})
print(restaurant1.colecao)
print(restaurant1.listar_itens_por_categoria('Prato'))'''

restaurant1 = Restaurante("Ponto do Sabor", "Centro")
restaurant1.adicionar_item({'nome': dish1.nome, 'categoria': 'Prato', 'preco': dish1.preco, 'notas': dish1.notas})
restaurant1.adicionar_item({'nome': dish2.nome, 'categoria': 'Prato', 'preco': dish2.preco, 'notas': dish2.notas})
restaurant1.adicionar_item({'nome': drink1.nome, 'categoria': 'Bebida', 'preco': drink1.preco, 'notas': drink1.notas})
restaurant1.adicionar_item({'nome': drink2.nome, 'categoria': 'Bebida', 'preco': drink2.preco, 'notas': drink2.notas})
restaurant1.adicionar_nota(4)
print("\nAverage of restaurants")
print(f"AVG {restaurant1.nome}: {restaurant1.consultar_media_ponderada()}")

restaurant2 = Restaurante("Trigo & Tomate", "Tijuca")
print(f"AVG {restaurant2.nome}: {restaurant2.consultar_media_ponderada()}")

# Customers

customer1 = Cliente("Taylan")
customer2 = Cliente("Gustavo")

customer1.favoritar_restaurante(restaurant1)
customer1.favoritar_restaurante(restaurant2)
print("\nFavorites first customer")
print(customer1.listar_favoritos())

customer2.favoritar_restaurante(restaurant2)
customer2.favoritar_restaurante(restaurant2)
customer2.desfavoritar_restaurante(restaurant1)
customer2.desfavoritar_restaurante(restaurant2)
print("\nFavorites second customer")
print(customer2.listar_favoritos())

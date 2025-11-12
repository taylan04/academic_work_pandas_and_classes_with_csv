from classes import *

dish1 = Prato("Strogonoff", 27.5, [5,4,5,5,4])
dish2 = Prato("Eggs with Rice", 9.99, [3,4,4,5,3])
drink1 = Bebida("Juice", 5.9, [5,5,5,5,5])
drink2 = Bebida("Water", 1.99, [5,5,5,5,5])
print(dish1.descricao())
print(dish2.descricao())

restaurant1 = Restaurante("Paris 6", "São Paulo")
restaurant1.adicionar_item({'nome': dish1.nome, 'categoria': 'Prato', 'preco': dish1.preco, 'notas': dish1.notas})
print(restaurant1.colecao)

restaurant2 = Restaurante("Casa Velha", "Rio de Janeiro")

customer1 = Cliente("Taylan")
customer2 = Cliente("Gustavo")

customer1.favoritar_restaurante(restaurant1)
customer1.favoritar_restaurante(restaurant2)
print(customer1.listar_favoritos())

customer2.favoritar_restaurante(restaurant2)
customer2.favoritar_restaurante(restaurant2)
customer2.desfavoritar_restaurante(restaurant1)
customer2.desfavoritar_restaurante(restaurant2)
print(customer2.listar_favoritos())

class Prato():
    def __init__(self,nome,preco,notas):
        self.nome = nome
        self.preco = preco
        self.notas = notas

    def descricao(self):
        return f"Prato: {self.nome} | Preço: {self.preco:.2f}"
    
class Bebida():
    def __init__(self,nome,preco,notas):
        self.nome = nome
        self.preco = preco
        self.notas = notas

    def descricao(self):
        return f"Bebida: {self.nome} | Preço da bebida: {self.preco:.2f}"
    
class Restaurante():
    def __init__(self,nome,bairro):
        self.nome = nome
        self.bairro = bairro
        self.colecao = []

    def adicionar_item(self, item):
        self.colecao.append(item)
    
    def buscar_item_por_nome(self, nome_item):
        for item in self.colecao:
            if nome_item.lower() == item.lower():
                return item
            else:
                return "\nItem não encontrado."
            
class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.restaurantes_favoritos = []

    def favoritar_restaurante(self, restaurante):
        self.restaurantes_favoritos.append(restaurante)
    
    def desfavoritar_restaurante(self, restaurante):
        if restaurante in self.restaurantes_favoritos:
            self.restaurantes_favoritos.remove(restaurante)
        else:
            print("Restaurante não encontrado.")

    def listar_favoritos(self):
        for restaurante in self.restaurantes_favoritos:
            print(f"\n{restaurante}")


#Part of it was written in Portuguese due to academic requirements.

class Prato():
    def __init__(self,nome,preco,notas):
        if len(nome) <= 2:
            raise ValueError("O nome do prato deve ter mais de 2 caracteres.")
        self.nome = nome
        if preco <= 0:
            raise ValueError("O preço do prato deve ser maior que zero.")
        self.preco = preco
        self.notas = notas

    def descricao(self):
        return f"Prato: {self.nome} | Preço: {self.preco:.2f}"
    
class Bebida():
    def __init__(self,nome,preco,notas):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
        self.nome = nome
        if preco <= 0:
            raise ValueError("O preço da bebida deve ser maior que zero.")
        self.preco = preco
        self.notas = notas

    def descricao(self):
        return f"Bebida: {self.nome} | Preço da bebida: {self.preco:.2f}"
    
class Restaurante():
    def __init__(self,nome,bairro):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
        self.nome = nome
        self.bairro = bairro
        self.colecao = []

    def adicionar_item(self, novo_item):
        if self.colecao:
            self.colecao.append(novo_item)

        for item in self.colecao:
            if item['nome'].lower() == novo_item['nome'].lower() or item['categoria'].lower() == novo_item['categoria'].lower():
                print("\nEsse item já existe.")
                return
            else:
                self.colecao.append(novo_item)
                print("\nItem adicionado.")
    
    def buscar_item_por_nome(self, nome_item):
        for item in self.colecao:
            if nome_item.lower() == item.lower():
                return item
            else:
                return "\nItem não encontrado."
        
    def listar_itens_por_categoria(self, categoria):
        for item in self.colecao:
            if item['categoria'] == categoria:
                print(f"\n{item}")
            
class Cliente():
    def __init__(self, nome):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
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


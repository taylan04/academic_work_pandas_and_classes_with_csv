#Part of it was written in Portuguese due to academic requirements.

class Prato():
    def __init__(self,nome,preco):
        if len(nome) <= 2:
            raise ValueError("O nome do prato deve ter mais de 2 caracteres.")
        self.nome = nome
        if preco <= 0:
            raise ValueError("O preço do prato deve ser maior que zero.")
        self.preco = preco
        self.notas = []

    def adicionar_nota(self, nota):
        if not (nota > 0 or nota < 6):
            raise ValueError("A nota deve estar entre 1 e 5.")
        self.notas.append(nota)

    def consultar_media(self):
        if not self.notas:
            return None
        return sum(self.notas) / len(self.notas)

    def descricao(self):
        return f"Prato: {self.nome} | Preço: {self.preco:.2f}"
    
class Bebida():
    def __init__(self,nome,preco):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
        self.nome = nome
        if preco <= 0:
            raise ValueError("O preço da bebida deve ser maior que zero.")
        self.preco = preco
        self.notas = []

    def adicionar_nota(self, nota):
        if not (nota > 0 or nota < 6):
            raise ValueError("A nota deve estar entre 1 e 5.")
        self.notas.append(nota)

    def consultar_media(self):
        if not self.notas:
            return None
        return sum(self.notas) / len(self.notas)

    def descricao(self):
        return f"Bebida: {self.nome} | Preço da bebida: {self.preco:.2f}"
    
class Restaurante():
    def __init__(self,nome,bairro):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
        self.nome = nome
        self.bairro = bairro
        self.colecao = []
        self.notas = []

    def adicionar_item(self, novo_item):
        if novo_item in self.colecao:
            print(f"\n O item {novo_item['nome']} já existe.")
            return
        else:
            self.colecao.append(novo_item)
            print(f"{novo_item['nome']} adicionado.")
            return
    
    def buscar_item_por_nome(self, nome_item):
        for item in self.colecao:
            if nome_item.lower() == item.lower():
                return item
            else:
                return "\nItem não encontrado."
            
    def adicionar_nota(self, nota):
        if not (nota > 0 or nota < 6):
            raise ValueError("A nota deve estar entre 1 e 5.")
        self.notas.append(nota)

    def consultar_media_ponderada(self):
        media_itens = 0
        for item in self.colecao:
            media_itens += len(item['notas'])
        if not self.notas and media_itens == 0:
            return None
        return len(self.notas) / media_itens
        
    def listar_itens_por_categoria(self, categoria):
        for item in self.colecao:
            if item['categoria'].lower() == categoria.lower():
                print(f"\n{item}")
            
class Cliente():
    def __init__(self, nome):
        if len(nome) <= 2:
            raise ValueError("O nome deve ter mais de 2 caracteres.")
        self.nome = nome
        self.restaurantes_favoritos = []

    def favoritar_restaurante(self, restaurante):
        if restaurante in self.restaurantes_favoritos:
            print("Restaurante já favoritado.")
            return
        self.restaurantes_favoritos.append(restaurante)
    
    def desfavoritar_restaurante(self, restaurante):
        if restaurante in self.restaurantes_favoritos:
            self.restaurantes_favoritos.remove(restaurante)
        else:
            print("Restaurante não encontrado.")

    def listar_favoritos(self):
        favoritos = []
        if not self.restaurantes_favoritos:
            return "Lista de favoritos vazia."

        for restaurante in self.restaurantes_favoritos:
            favoritos.append(restaurante.nome)
        return favoritos


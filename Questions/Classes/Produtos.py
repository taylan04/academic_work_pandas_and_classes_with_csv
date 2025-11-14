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
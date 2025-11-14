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
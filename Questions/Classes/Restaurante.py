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
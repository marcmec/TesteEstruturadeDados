class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self,item):
        self.itens.append(item)

    def remover(self):
        if self.itens:
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

    def inversao(self):
        for item in self.itens[::-1]:
            print(item)

fila = Fila()
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)

fila.inversao()

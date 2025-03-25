class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if self.item:
            return self.item.pop(0)
        return None

    def vazia(self):
        return len(self.items) == 0


fila = Fila()
fila.adicionar(1)
fila.adicionar(2)

if not fila.vazia():
    print(fila.remover())

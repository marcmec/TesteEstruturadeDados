class Fila:
    def __init__(self):
        self.itens = []
    def adicionar(self, item):
        self.itens.append(item)
    def remover(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            raise IndexError("Fila vazia!")
    def vazia(self):
        return len(self.itens) == 0
    def inverter(self):
        self.itens = self.itens[::-1]
    def __str__(self):
        return str(self.itens)
fila = Fila()
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)
fila.inverter()
print(fila)
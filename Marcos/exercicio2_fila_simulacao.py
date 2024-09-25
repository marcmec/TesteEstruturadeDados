class Fila:
    def __init__(self):
        self.itens = []
    def enfileirar(self, item):
        self.itens.append(item)
    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            raise IndexError("Fila vazia!")
    def vazia(self):
        return len(self.itens) == 0
    def __str__(self):
        return str(self.itens)
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
item_removido = fila.desenfileirar()
print("Item removido:", item_removido)  
class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.estaVazia():
            self.items.pop(0)
        else:
            return None

    def estaVazia(self):
        return len(self.items) == 0

    def inverterFila(self):
        for i in range(len(self.items)):
            pass
        self.items.reverse()

if __name__ == "__main__":

    fila = Fila()

    print(fila.items)

    print(fila.enfileirar(1), fila.enfileirar(2), fila.enfileirar(3))

    print("Adicionado os valores:", fila.items)

    print(fila.inverterFila())

    print(fila.items)

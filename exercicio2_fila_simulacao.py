class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def estaVazia(self):
        return len(self.items) == 0

    def desenfileirar(self):
        if not self.estaVazia():
            print(f"Valor [{self.items.pop(0)}] removido")
        else:
            return None

if __name__ == "__main__":

    fila = Fila()

    print(fila.items)

    print(fila.enfileirar(1), fila.enfileirar(2))

    print("Adicionado os valores:", fila.items)

    fila.desenfileirar()

    print("Apos remoção do valor da fila:", fila.items)

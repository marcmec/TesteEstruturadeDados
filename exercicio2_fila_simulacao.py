class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

def main():
    fila = Fila()

    print("Entrada: [ ]")
    fila.enfileirar(1)
    fila.enfileirar(2)
    print("Enfileirando 1 e 2...")

    saida = fila.desenfileirar()
    print(f"Saída: {saida}")

if __name__ == "__main__":
    main()
class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def tamanho(self):
        return len(self.itens)

def simulacao_fila():
    fila = Fila()

    fila.enfileirar(1)
    fila.enfileirar(2)

    resultado = fila.desenfileirar()

    return resultado

if __name__ == "__main__":
    resultado = simulacao_fila()
    print(f"Elemento desenfileirado: {resultado}")

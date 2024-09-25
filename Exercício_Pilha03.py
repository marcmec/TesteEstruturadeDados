class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

def inverter_fila(fila):
    pilha = []
    
    while not fila.esta_vazia():
        pilha.append(fila.desenfileirar())
    
    for item in reversed(pilha):
        fila.enfileirar(item)

fila = Fila()
for numero in [1, 2, 3]:
    fila.enfileirar(numero)

inverter_fila(fila)

saida = [fila.desenfileirar() for _ in range(fila.tamanho())]
print(saida)  # Saída: [3, 2, 1]
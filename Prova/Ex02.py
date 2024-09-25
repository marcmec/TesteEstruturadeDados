class Fila:
    def __init__(self):
        self.itens = []
    
    def estaVazia(self):
        return len(self.itens) == 0
    
    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.estaVazia():
            return self.itens.pop(0)
        else:
            return "A fila esta vazia!"

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

print(f"Fila atual: {fila.itens}")
print(f"Desenfileirar: {fila.desenfileirar()}")
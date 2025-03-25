from collections import deque

class Fila:
    def __init__(self):
        self.itens = deque()
    
    def enfileirar(self, item):
        self.itens.append(item)
    
    def desenfileirar(self):
        return self.itens.popleft() if self.itens else None

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
print(fila.desenfileirar())
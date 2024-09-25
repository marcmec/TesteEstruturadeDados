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

def reverter_fila(fila):
    pilha = []
    
    while not fila.esta_vazia():
        pilha.append(fila.desenfileirar())

    for palavra in pilha:
        fila.enfileirar(palavra)
        
fila = Fila()

fila.enfileirar("maçã")
fila.enfileirar("banana")
fila.enfileirar("laranja")

reverter_fila(fila)

resultado = []
while not fila.esta_vazia():
    resultado.append(fila.desenfileirar())

print(resultado)

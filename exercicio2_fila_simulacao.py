#Exercício 02

class Fila:
    def __init__(self):
        self.valores = []
    
    def enfileirar(self, valor):
        self.valores.append(valor)
    
    def desenfileirar(self):
        self.valores.pop(0)
        
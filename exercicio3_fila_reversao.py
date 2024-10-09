#Exercício 03

class FilaReversa:
    def __init__(self):
        self.valores = []

    def enfileirar(self, valor): 
        self.valores = [valor] + self.valores
        
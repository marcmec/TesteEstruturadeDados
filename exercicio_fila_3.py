class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, val):
        self.fila.insert(0, val)

    def desenfileirar(self):
        self.fila.pop()

    def imprimir(self):
        for i in self.fila:
            print(i)
    
    
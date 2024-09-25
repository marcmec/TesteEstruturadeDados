class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, valor):
        self.itens.append(valor)

    def desenfileirar(self):
        if len(self.itens) == 0:
            return None
        else:
            return self.itens.pop(0)

    
if __name__ == "__main__":

    fila = Fila()

    fila.enfileirar(1)
    fila.enfileirar(2)
    print(fila.desenfileirar())
    


    

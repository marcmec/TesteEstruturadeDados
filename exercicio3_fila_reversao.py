class FilaInvertida:
    def __init__(self):
        self.itens = []

    def enfileirar(self, valor):
        self.itens.append(valor)

    def desenfileirar(self):
      if len(self.itens) == 0:
        print('Fila Vazia')
        return None

      else:
        return self.itens.pop(0)

    def inverter(self):
        pilha = []
        
        while self.itens:
            pilha.append(self.desenfileirar())
        

        while pilha:
            self.enfileirar(pilha.pop())

    def obter_fila(self):
        return self.itens


fila = FilaInvertida()

for elemento in [1, 2, 3]:
    fila.enfileirar(elemento)


fila.inverter()


resultado = fila.obter_fila()
print(resultado)  

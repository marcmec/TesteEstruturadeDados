class Fila:

    def __init__ (self):
      self.itens = []

    def enfileirar(self,valor):
       self.itens.append(valor)

    def desenfileirar(self):
      if len(self.itens) == 0:
        print('Fila Vazia')
        return None

      else:
        print(f'O número retirado foi {self.itens[0]}')
        return self.itens.pop(0)

  


fila = Fila()

fila.enfileirar(1)
fila.enfileirar(2)
print(fila.itens)
fila.desenfileirar()
print(fila.itens)

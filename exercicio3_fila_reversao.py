class Fila:
  def __init__(self) -> None:
    self.itens = []


  def enfileirar(self, val):
    self.itens.append(val)

  def desenfileirar(self):
    if self.itens:
      return self.itens.pop(0)

def reverse(fila):
  reversed = []
  for i in range(len(fila.itens) - 1, -1, -1):
    reversed.append(fila.itens[i])
  return reversed

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print(reverse(fila))

        
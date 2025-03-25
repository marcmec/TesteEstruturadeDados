class Fila:
    def __init__(self):
        self.items = [ ]

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "A Fila está vazia!"

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
resultado = fila.dequeue()

print(f"Resultado do Dequeue : {resultado}")
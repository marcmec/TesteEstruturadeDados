class Fila:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "A fila está vazia!"
        
    def reverse(self):
        stack = [ ]
        while not self.isEmpty():
            stack.append(self.dequeue())
        while stack:
            self.enqueue(stack.pop())
        
fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.reverse()
print(f"Fila no reverse: {list(fila.items)}")

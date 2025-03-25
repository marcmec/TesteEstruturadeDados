class Pilha:
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        return self.itens.pop() if self.itens else None
    
    def is_empty(self):
        return len(self.itens) == 0

def inverter_string(s):
    pilha = Pilha()
    for char in s:
        pilha.push(char)
    return "".join(pilha.pop() for _ in range(len(s)))

print(inverter_string("Hello"))
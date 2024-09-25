class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()

    def esta_vazia(self):
        return len(self.items) == 0

def inverter_string(s):
    pilha = Pilha()
    
    for char in s:
        pilha.empilhar(char)

    string_invertida = ''
    while not pilha.esta_vazia():
        string_invertida += pilha.desempilhar()

    return string_invertida

entrada = "Guilherme"
saida = inverter_string(entrada)
print(saida)  

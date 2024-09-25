class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

def inverter_string(s):
    pilha = Pilha()
    
    for caractere in s:
        pilha.empilhar(caractere)
    
    string_invertida = ""
    
    while not pilha.esta_vazia():
        string_invertida += pilha.desempilhar()
    
    return string_invertida

def inverter_palavras(palavras):
    return [inverter_string(palavra) for palavra in palavras]

entrada = ["Hello", "World", "Python", "Pilha"]
saida = inverter_palavras(entrada)
print(saida)

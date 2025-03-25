class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return self.itens == []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def tamanho(self):
        return len(self.itens)

def inverter_string(texto):
    pilha = Pilha()

    for caractere in texto:
        pilha.empilhar(caractere)

    texto_invertido = ""
    while not pilha.esta_vazia():
        texto_invertido += pilha.desempilhar()
        
    return texto_invertido

if __name__ == "__main__":
    entrada = "Hello"
    resultado = inverter_string(entrada)
    print(f"String original: {entrada}")
    print(f"String invertida: {resultado}")

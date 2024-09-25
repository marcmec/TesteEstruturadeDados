class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def mostrar(self):
        return self.itens

def main():
    fila = Fila()
    numeros = []

    while True:
        entrada = input("Insira um número inteiro (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            numero = int(entrada)
            fila.enfileirar(numero)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    print("Números inseridos em ordem reversa:", numeros[::-1])

if __name__ == "__main__":
    main()
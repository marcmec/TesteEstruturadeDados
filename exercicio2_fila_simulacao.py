class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens = self.itens + [item]
        print(self.itens)

    def desenfileirar(self):
        if len(self.itens) == 0:
            print("A fila está vazia.")
            return None
        
        primeiro = self.itens[0]  
        self.itens = self.itens[1:]  
        
        print(f"Número removido: {primeiro}")
        print(f"Números restantes na fila: {self.itens}" if self.itens else "A fila agora está vazia.")
        
        return primeiro 
    
fila = Fila()


while True: 
    resposta = int(input("Deseja fazer qual operação (1- Enfileirar, 2- Desenfileirar, 0- finalizar): "))

    if resposta == 1:
        numero = input("Dig1ite o numero que quer colocar na fila: ")
        print(f"Você colocou o numero " + numero + " na fila.")
        fila.enfileirar(numero)

    if resposta == 2:
        fila.desenfileirar()
    
    if resposta == 0:
        break

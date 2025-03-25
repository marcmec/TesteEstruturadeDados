class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def insert(self, value):
        node = Node(value)
        if self.raiz == None:
            self.raiz = node
        else:
            current = self.raiz
            while True:
                parent = current
                if node.valor < current.valor:
                    current = current.esquerda
                    if current == None:
                        parent.esquerda = node
                        return
                else:
                    current = current.direita
                    if current == None:
                        parent.direita = node
                        return

    def imprimir_filhos_raiz(self):
        if self.raiz:
            print(f"Filho da raiz: {self.raiz.esquerda.valor , self.raiz.direita.valor}")
        else:
            print("Árvore vazia.")

arvore = ArvoreBinaria()

numbers_input = input("Insira os números (separado por vírgula e espaço): ")
for i in numbers_input.split(", "):
    arvore.insert(int(i))

arvore.imprimir_filhos_raiz()

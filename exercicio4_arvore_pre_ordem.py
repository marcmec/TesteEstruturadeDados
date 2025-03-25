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
                    
    def pre_ordem(self, node):
        if node != None:
            print(node.valor, end=" ")
            self.pre_ordem(node.esquerda)
            self.pre_ordem(node.direita) 
    
arvore = ArvoreBinaria()

numbers_input = input("Insira os números (separado por vírgula e espaço): ")
for i in numbers_input.split(", "):
    arvore.insert(int(i))

print("Pre ordem: ")
arvore.pre_ordem(arvore.raiz)
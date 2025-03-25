class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class binaryTree:
    def __init__(self, raiz=None):
        self.raiz = raiz

raiz = Node(10)
arvore = binaryTree(raiz)
print("Árvore criada com raiz:", arvore.raiz.valor)
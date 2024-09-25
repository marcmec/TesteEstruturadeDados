class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._insert(self.root, valor)

    def _insert(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.left is None:
                no_atual.left = Node(valor)
            else:
                self._insert(no_atual.left, valor)
        elif valor > no_atual.valor:
            if no_atual.right is None:
                no_atual.right = Node(valor)
            else:
                self._insert(no_atual.right, valor)
        else:
            print("Valor já existente na árvore.")

    def busca(self, valor):
        return self._busca(self.root, valor)

    def _busca(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._busca(no_atual.left, valor)
        else:
            return self._busca(no_atual.right, valor)

    def inorderTraversal(self):
        elementos = []
        self._inorder(self.root, elementos)
        return elementos
    
    def _inorder(self, no_atual, elementos):
        if no_atual:
            self._inorder(no_atual.left, elementos)
            elementos.append(no_atual.valor)
            self._inorder(no_atual.right, elementos)

arvore = ArvoreBinaria()
arvore.insert(21)
arvore.insert(18)
arvore.insert(1)
arvore.insert(5)
arvore.insert(11)
arvore.insert(34)
arvore.insert(10)

print("Árvore Em Ordem: ", arvore.inorderTraversal())
print("Buscar por 11: ", arvore.busca(11))
print("Buscar por 34: ", arvore.busca(34))
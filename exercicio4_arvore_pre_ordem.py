class Arvore_busca_binaria:
    def __init__(self, node):
        self.node = node
        self.esquerda = None
        self.direita = None

    def insert(self, node):
        if node < self.node:
            if self.esquerda is None:
                self.esquerda = Arvore_busca_binaria(node)
            else:
                self.esquerda.insert(node)
        else:
            if self.direita is None:
                self.direita = Arvore_busca_binaria(node)
            else:
                self.direita.insert(node)

    def pre_order(self):
        print(self.node)
        if self.esquerda:
            self.esquerda.pre_order()
        if self.direita:
            self.direita.pre_order()



arvore = Arvore_busca_binaria(6)
arvore.insert(5)
arvore.insert(4)
arvore.insert(6)
arvore.insert(8)
arvore.insert(7)
arvore.insert(9)

arvore.pre_order()
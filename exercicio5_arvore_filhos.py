class Arvore_busca_binaria:
    def __init__(self, node):
        self.node = node
        self.esquerda = None
        self.direita = None

    def inserir(self, node):
        if node < self.node:
            if self.esquerda is None:
                self.esquerda = Arvore_busca_binaria(node)
            else:
                self.esquerda.inserir(node)
        else:
            if self.direita is None:
                self.direita = Arvore_busca_binaria(node)
            else:
                self.direita.inserir(node)

    def pre_order(self):
        print(self.node)
        if self.esquerda:
            self.esquerda.pre_order()
        if self.direita:
            self.direita.pre_order()

    def imprimir_filhos(self):
        filhos = []
        if self.esquerda:
            filhos.append(self.esquerda.node)
        if self.direita:
            filhos.append(self.direita.node)

        if filhos:
            print(filhos)



arvore = Arvore_busca_binaria(10)
arvore.inserir(5)
arvore.inserir(15)

arvore.imprimir_filhos()
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._adicionar_recursivo(self.raiz, valor)

    def _adicionar_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._adicionar_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._adicionar_recursivo(no_atual.direita, valor)

    def imprimir(self):
        self._imprimir_recursivo(self.raiz)

    def _imprimir_recursivo(self, no_atual):
        if no_atual is not None:
            self._imprimir_recursivo(no_atual.esquerda)
            print(no_atual.valor)
            self._imprimir_recursivo(no_atual.direita)

arvore = ArvoreBinaria()
arvore.adicionar(10)
arvore.adicionar(5)
arvore.adicionar(15)
arvore.adicionar(3)

print("Elementos da árvore em ordem:")
arvore.imprimir()
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    def adicionar(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._adicionar_recursivo(self.raiz, valor)
    def _adicionar_recursivo(self, no_atual, valor):
        if no_atual.esquerdo is None:
            no_atual.esquerdo = No(valor)
        elif no_atual.direito is None:
            no_atual.direito = No(valor)
        else:
            self._adicionar_recursivo(no_atual.esquerdo, valor)
    def percorrer_pre_ordem(self):
        return self._percorrer_pre_ordem_recursivo(self.raiz)
    def _percorrer_pre_ordem_recursivo(self, no_atual):
        if no_atual is None:
            return []
        return [no_atual.valor] + self._percorrer_pre_ordem_recursivo(no_atual.esquerdo) + self._percorrer_pre_ordem_recursivo(no_atual.direito)
arvore = ArvoreBinaria()
arvore.adicionar(1)
arvore.adicionar(2)
arvore.adicionar(3)
arvore.adicionar(4)
arvore.adicionar(5)
resultado = arvore.percorrer_pre_ordem()
print("Valores na árvore:", resultado)

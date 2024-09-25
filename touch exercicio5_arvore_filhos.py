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
    def identificar_filhos(self):
        self._identificar_filhos_recursivo(self.raiz)
    def _identificar_filhos_recursivo(self, no_atual):
        if no_atual:
            filhos = [no_atual.esquerdo.valor if no_atual.esquerdo else None,
                      no_atual.direito.valor if no_atual.direito else None]
            print(f"Nó: {no_atual.valor}, Filhos: {list(filter(None, filhos))}")
            self._identificar_filhos_recursivo(no_atual.esquerdo)
            self._identificar_filhos_recursivo(no_atual.direito)
arvore = ArvoreBinaria()
arvore.adicionar(1)
arvore.adicionar(2)
arvore.adicionar(3)
arvore.adicionar(4)
arvore.adicionar(5)
arvore.identificar_filhos()
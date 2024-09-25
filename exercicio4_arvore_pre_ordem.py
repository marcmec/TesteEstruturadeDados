
class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.filho_esquerdo = None
        self.filho_direito = None

class ArvoreBinaria:
    def __init__(self) -> None:
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, no_atual):
        if valor <= no_atual.valor:
            if no_atual.filho_esquerdo is None:
                no_atual.filho_esquerdo = No(valor)
            else:
                self._inserir(valor, no_atual.filho_esquerdo)
        else:
            if no_atual.filho_direito is None:
                no_atual.filho_direito = No(valor)
            else:
                self._inserir(valor, no_atual.filho_direito)

    def mostrar_em_ordem(self, no=None):
        if no is None:
            no = self.raiz
            print("Exibindo em ordem:", end=" ")
        if no.filho_esquerdo:
            self.mostrar_em_ordem(no.filho_esquerdo)
        print(no.valor, end=" ")
        if no.filho_direito:
            self.mostrar_em_ordem(no.filho_direito)

    def mostrar_pre_ordem(self, no=None):
        if no is None:
            no = self.raiz
            print("Exibindo pré-ordem:", end=" ")
        print(no.valor, end=" ")
        if no.filho_esquerdo:
            self.mostrar_pre_ordem(no.filho_esquerdo)
        if no.filho_direito:
            self.mostrar_pre_ordem(no.filho_direito)

arvore = ArvoreBinaria()
valores = [99, 50, 74, 22, 19, 21, 2, 5]
for v in valores:
    arvore.inserir(v)

arvore.mostrar_pre_ordem()
print()
arvore.mostrar_em_ordem()

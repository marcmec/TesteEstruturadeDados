class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self) -> None:
        self.raiz = None

    def adicionar(self, valor):
        novo_no = self._adicionar(valor, self.raiz)
        if not self.raiz:
            self.raiz = novo_no

    def _adicionar(self, valor, no_atual):
        if no_atual is None:
            return No(valor)

        if valor <= no_atual.valor:
            no_atual.esquerda = self._adicionar(valor, no_atual.esquerda)
        else:
            no_atual.direita = self._adicionar(valor, no_atual.direita)
        return no_atual

    def em_ordem(self):
        print("Em ordem:", end=" ")
        self._em_ordem(self.raiz)
        print()

    def _em_ordem(self, no_atual):
        if no_atual is None:
            return

        self._em_ordem(no_atual.esquerda)
        print(no_atual.valor, end=" ")
        self._em_ordem(no_atual.direita)

    def pre_ordem(self):
        print("Pré ordem:", end=" ")
        self._pre_ordem(self.raiz)
        print()

    def _pre_ordem(self, no_atual):
        if no_atual is None:
            return

        print(no_atual.valor, end=" ")
        self._pre_ordem(no_atual.esquerda)
        self._pre_ordem(no_atual.direita)

# Exemplo de uso
arvore_binaria = ArvoreBinaria()
arvore_binaria.adicionar(30)
arvore_binaria.adicionar(50)
arvore_binaria.adicionar(35)
arvore_binaria.adicionar(15)


arvore_binaria.pre_ordem()
arvore_binaria.em_ordem()

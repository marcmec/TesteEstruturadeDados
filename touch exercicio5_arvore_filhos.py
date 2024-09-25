class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if not self.raiz:
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

    def percurso_pre_ordem(self, no):
        if no:
            print(no.valor, end=' ')
            self.percurso_pre_ordem(no.esquerda)
            self.percurso_pre_ordem(no.direita)

    def obter_filhos(self, valor):
        no = self.buscar(self.raiz, valor)
        if no:
            filhos = []
            if no.esquerda:
                filhos.append(no.esquerda.valor)
            if no.direita:
                filhos.append(no.direita.valor)
            return filhos
        return None

    def buscar(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)
        else:
            return self.buscar(no.direita, valor)

arvore = ArvoreBinaria()

arvore.adicionar(13)
arvore.adicionar(1)
arvore.adicionar(20)
arvore.adicionar(2)
arvore.adicionar(4)
arvore.adicionar(11)
arvore.adicionar(14)

print("Percurso em pré-ordem:")
arvore.percurso_pre_ordem(arvore.raiz)
print()

filhos_de_13 = arvore.obter_filhos(13)
print("Filhos do nó 13:", filhos_de_13)

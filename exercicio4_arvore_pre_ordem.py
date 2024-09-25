class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, valor_raiz):
        self.raiz = No(valor_raiz)

    def inserir(self, valor):
        if valor < self.raiz.valor:
            if self.raiz.esquerda is None:
                self.raiz.esquerda = No(valor)
            else:
                self._inserir_recursivo(self.raiz.esquerda, valor)
        else:
            if self.raiz.direita is None:
                self.raiz.direita = No(valor)
            else:
                self._inserir_recursivo(self.raiz.direita, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def obter_filhos(self):
        filhos = []
        if self.raiz.esquerda:
            filhos.append(self.raiz.esquerda.valor)
        if self.raiz.direita:
            filhos.append(self.raiz.direita.valor)
        return filhos

arvore = ArvoreBinaria(10)
arvore.inserir(5)
arvore.inserir(15)

saida = arvore.obter_filhos()
print(saida)
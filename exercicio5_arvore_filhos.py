class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivamente(no_atual.direita, valor)

    def obter_filhos(self, valor):
        no = self._buscar_no(self.raiz, valor)
        if no:
            filhos = []
            if no.esquerda:
                filhos.append(no.esquerda.valor)
            if no.direita:
                filhos.append(no.direita.valor)
            return filhos
        return None

    def _buscar_no(self, no_atual, valor):
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        if valor < no_atual.valor:
            return self._buscar_no(no_atual.esquerda, valor)
        return self._buscar_no(no_atual.direita, valor)

arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)

resultado = arvore.obter_filhos(10)
print(resultado)

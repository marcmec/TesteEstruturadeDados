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
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    def percurso_pre_ordem(self):
        elementos = []
        self._pre_ordem_recursivo(self.raiz, elementos)
        return elementos

    def _pre_ordem_recursivo(self, no, elementos):
        if no:
            elementos.append(no.valor)
            self._pre_ordem_recursivo(no.esquerda, elementos)
            self._pre_ordem_recursivo(no.direita, elementos)

if __name__ == "__main__":
    arvore = ArvoreBinaria()
    valores = [10, 5, 15, 3, 7, 12, 18]

    for valor in valores:
        arvore.inserir(valor)

    print("Percurso em pré-ordem:")
    print(arvore.percurso_pre_ordem())

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.di = None
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self._inserir_recursivo(no.esq, valor)
        else:
            if no.di is None:
                no.di = No(valor)
            else:
                self._inserir_recursivo(no.di, valor)


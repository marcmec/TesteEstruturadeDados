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
            self.inserir_recursivo(self.raiz, valor)
    def inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self.inserir_recursivo(no.esq, valor)
        else:
            if no.di is None:
                no.di = No(valor)
            else:
                self.inserir_recursivo(no.di, valor)                
    def retornar_filhos(self, valor):
        no = self.buscar_no(self.raiz, valor)
        if no:
            filhos = []
            if no.esq:
                filhos.append(no.esq.valor)
            if no.di:
                filhos.append(no.di.valor)
            return filhos
        return None
    def buscar_no(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self.buscar_no(no.esq, valor)
        else:
            return self.buscar_no(no.di, valor)


arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(4)
arvore.inserir(6)
#pede pra printar

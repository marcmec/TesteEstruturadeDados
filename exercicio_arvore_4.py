class Arvore:
    def __init__(self):
        self.raiz = None

    def adicionar_no(self, val):
        if self.raiz:
            if val < self.raiz.valor:
                if self.raiz.fesq:
                    self.raiz.fesq.adicionar_no(val)
                else:
                    self.raiz.fesq = No(val)
            if val > self.raiz.valor:
                if self.raiz.fdir:
                    self.raiz.fdir.adicionar_no(val)
                else:
                    self.raiz.fdir = No(val)
            else:
                print("Esse número já existe na árvore.")
        else:
            self.raiz = No(val)



class No:
    def __init__(self, valor):
        self.valor = valor
        self.fesq = None
        self.fdir = None

    def adicionar_no(self, val):
        if val < self.valor:
                if self.fesq:
                    self.fesq.adicionar_no(val)
                else:
                    self.fesq = No(val)
            if val > self.valor:
                if self.fdir:
                    self.fdir.adicionar_no(val)
                else:
                    self.fdir = No(val)
            else:
                print("Esse número já existe na árvore.")

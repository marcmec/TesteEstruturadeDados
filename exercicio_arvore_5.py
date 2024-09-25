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
    
    def listar_filhos(self, val):
        lista_fs = []
        if self.raiz:
            if val < self.raiz.valor:
                if self.raiz.fesq:
                    self.raiz.fesq.listar_filhos(val)
                else:
                    print("Esse numero não existe na arvore.")
            if val > self.raiz.valor:
                if self.raiz.fdir:
                    self.raiz.fdir.listar_filhos(val)
                else:
                    print("Esse numero não existe na arvore.")
            else:
                lista_fs.append(self.raiz.fesq.valor)
                lista_fs.append(self.raiz.fdir.valor)
                print(lista_fs)
        else:
            print("A árvore está vazia.")


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

    def listar_filhos(self, val):
        lista_fs = []
        if val < self.valor:
                if self.fesq:
                    self.fesq.listar_filhos(val)
                else:
                    print("Esse numero não existe na arvore.")
        if val > self.valor:
                if self.fdir:
                    self.fdir.listar_filhos(val)
                else:
                    print("Esse numero não existe na arvore.")
        else:
                lista_fs.append(self.fesq.valor)
                lista_fs.append(self.fdir.valor)
                print(lista_fs)


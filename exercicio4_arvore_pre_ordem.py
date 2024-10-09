#Exercício 04

class No:
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_filho(self.raiz, valor)
    
    def inserir_filho(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self.inserir_filho(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self.inserir_filho(no_atual.direita, valor)

arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)

cont = [1, 3, 5]

def dfs(raiz):
    if not raiz:
        return None

    cont.append(raiz.valor)
    dfs(raiz.esquerda.valor)
    dfs(raiz.direita.valor)
    
cont.pop(0)
print(cont)
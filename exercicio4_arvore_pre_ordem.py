class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def pre_ordem(self, no, resultado=[]):
        if no:
            resultado.append(no.valor)
            self.pre_ordem(no.esquerda, resultado)
            self.pre_ordem(no.direita, resultado)
        return resultado

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def obterFilhos(no):
    filhos = []
    if no.esquerda:
        filhos.append(no.esquerda.valor)
    if no.direita:
        filhos.append(no.direita.valor)
    return filhos

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)

saida = obterFilhos(raiz)
print(saida)

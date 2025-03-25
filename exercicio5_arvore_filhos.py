class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor, filho_esquerda=None, filho_direita=None):
        novo_no = No(valor)

        if filho_esquerda is not None:
            novo_no.esquerda = No(filho_esquerda)

        if filho_direita is not None:
            novo_no.direita = No(filho_direita)

        if self.raiz is None:
            self.raiz = novo_no

        return novo_no

    def obter_filhos(self, no):
        filhos = []

        if no.esquerda:
            filhos.append(no.esquerda.valor)

        if no.direita:
            filhos.append(no.direita.valor)

        return filhos

if __name__ == "__main__":
    arvore = ArvoreBinaria()
    raiz = arvore.inserir(10, 5, 15)

    filhos = arvore.obter_filhos(raiz)
    print(f"Valor do nó: {raiz.valor}")
    print(f"Filhos: {filhos}")

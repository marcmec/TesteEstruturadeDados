class Arvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir(self,novoValor):
        if novoValor < self.valor:
            if self.esquerda is None:
                self.esquerda = Arvore(novoValor)
            else:
                self.esquerda = self.esquerda.inserir(novoValor)

        elif novoValor > self.valor:
            if self.direita is None:
                self.direita = Arvore(novoValor)
            else:
                self.direita = self.direita.inserir(novoValor)

    def percorrimento(self):
        elementos = []
        if self.esquerda:
            elementos += self.esquerda.inserir()
        if self.direita:
            elementos += self.direita.inserir()
        return elementos


if __name__ == "__main__":
    arvore = Arvore(1)

    arvore.inserir(2)
    arvore.inserir(3)
    arvore.inserir(4)
    arvore.inserir(5)

    arvore.percorrimento()
def obter_filhos(no):
    filhos = []
    if no.esquerda:
        filhos.append(no.esquerda.valor)
    if no.direita:
        filhos.append(no.direita.valor)
    return filhos

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
print(obter_filhos(raiz))
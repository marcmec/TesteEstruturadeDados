class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def obter_filhos(node):
    filhos = []
    if node.esquerda:
        filhos.append(node.esquerda.valor)
    if node.direita:
        filhos.append(node.direita.valor)
    return filhos

raiz = Node(10)
raiz.esquerda = Node(5)
raiz.direita = Node(15)
saida = obter_filhos(raiz)
print(f"Entrada: 10 (filhos: 5, 15)")
print(f"Saída: {saida}")
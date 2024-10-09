#Exercício 05

cont = []

def dfs(no):
    if not no:
        return None
    
    cont.append(no.valor)
    dfs(no.esquerda)
    dfs(no.direita)

filhos_arvore = dfs(arvore)
filhos_arvore.pop(0)
print(filhos_arvore)

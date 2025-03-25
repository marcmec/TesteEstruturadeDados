# Árvore: Filhos

# Nó
class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None  
        self.right = None  

def filhos(no):
    filhos = [] 
    # Se tiver filho na esquerda
    if no.left: 
        filhos.append(no.left.value)  
    # Se tiver filho na direita
    if no.right: 
        filhos.append(no.right.value) 
    return filhos  

# Criando a árvore
root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(filhos(root))  

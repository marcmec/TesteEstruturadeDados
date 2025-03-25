# Árvore: Crie uma estrutura de árvore binária

# Nó
class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None  
        self.right = None  

# Criando a árvore binária
root = Node(10)  
root.left = Node(5) 
root.right = Node(15)  #

# Mostrando os valores dos nós
print(root.value) 
print(root.left.value)  
print(root.right.value)  

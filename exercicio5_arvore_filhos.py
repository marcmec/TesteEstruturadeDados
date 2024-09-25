class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(2)
raiz.esquerda.direita = No(7)



def mostrar_filhos(no):
    if No is None:
        print("O nó está vazio.")
        return
    
    filhos = []
    
    if no.esquerda is not None:
        filhos.append(no.esquerda.valor)
    
    if no.direita is not None:
        filhos.append(no.direita.valor)
    
    if filhos:
        print(f"Filhos de {no.valor}: {filhos}")
    else:
        print(f"O nó {no.valor} não tem filhos.")


mostrar_filhos(raiz) 
mostrar_filhos(raiz.esquerda)
mostrar_filhos(raiz.direita)


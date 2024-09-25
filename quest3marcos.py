def reverter_fila(fila):
    pilha = []
    while fila:
        pilha.append(fila.pop(0))
    while pilha:
        fila.append(pilha.pop())
    
    return fila

fila = [1, 2, 3]
fila_revertida = reverter_fila(fila)
print("Fila ao contrario:", fila_revertida)
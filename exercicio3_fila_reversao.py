def inverter_fila(fila):
    pilha = [] 

    while len(fila) > 0:
        pilha += [fila[0]] 
        fila = fila[1:]  


    while len(pilha) > 0:
        fila += [pilha[-1]]  
        pilha = pilha[:-1] 

    return fila 

fila = [1, 2, 3]
fila_invertida = inverter_fila(fila)
print(fila_invertida) 
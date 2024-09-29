def reversao_fila(elementos):
    fila = list(elementos)
    fila_reversa = []
    
    while fila:
        fila_reversa.append(fila.pop())
    
    return fila_reversa

resultado = reversao_fila([1, 2, 3])
print(resultado)

def fila_simulacao(fila):
    fila.append(1)
    fila.append(2)
    primeiro_elemento = fila.pop(0)
    return primeiro_elemento

fila_inicial = []
resultado = fila_simulacao(fila_inicial)
print(resultado)


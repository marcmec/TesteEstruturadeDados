def inverter_string(novoValor):
    pilha = []
    for letra in novoValor:
        pilha.append(letra)
    string_invertida = ''
    while pilha:
        string_invertida += pilha.pop()

    return string_invertida


entrada = "Hello"
saida = inverter_string(entrada)
print(saida)

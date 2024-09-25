def inverter_string(com_string):
    pilha = []
    for caractere in com_string:
        pilha.append(caractere)
    string_invertida = ""
    while pilha:
        string_invertida += pilha.pop()
    return string_invertida
entrada = "hello"
saida = inverter_string(entrada)
print(saida)
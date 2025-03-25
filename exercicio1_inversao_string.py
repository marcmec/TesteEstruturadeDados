def inverter_string(text):
    pilha = []
    palavra_invertida = ""

    for char in text:
        pilha.append(char)

    
    while pilha:
        palavra_invertida += pilha.pop()

    
    return palavra_invertida


palavra = "Hello"
resultado = inverter_string(palavra)
print(resultado)

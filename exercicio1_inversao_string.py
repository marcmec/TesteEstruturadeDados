#Exercício 01

def inverter_string(string):
    pil = []

    for i in string:
        pilha.append(i)

    string_invertida = ""
    while pil:
        string_invertida += pilha.pop()

    return string_invertida

txt = "Hello"
txt = inverter_string(txt)

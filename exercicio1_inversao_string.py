def inversao_pilha(s):
    pilha = list(s)
    pilha_invertida = ""
    
    while pilha:
        pilha_invertida += pilha.pop()
    
    return pilha_invertida

resultado = inversao_pilha("Hello")
print(resultado)
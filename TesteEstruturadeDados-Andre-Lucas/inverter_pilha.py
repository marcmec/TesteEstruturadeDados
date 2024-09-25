def inversao_pilha(s):
    pilha = []
    for  char in s:
        pilha.append(char)
        pilha_invertida = ""
    while pilha:
        pilha_invertida += pilha.pop()
    return pilha_invertida

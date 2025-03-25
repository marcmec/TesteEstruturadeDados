# Inversão de string usando pilha

def inversao_string(texto):
    pilha = []

    for char in texto:
        pilha.append(char)
    
    string_invertida = ""
    while len(pilha) > 0:
        # Retira o ultimo caractere e coloca na pilha
        string_invertida += pilha.pop()
    
    return string_invertida

# Testando
entrada = "Hello"
print(inversao_string(entrada))

    

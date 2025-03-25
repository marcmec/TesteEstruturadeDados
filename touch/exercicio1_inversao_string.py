def reverseString(s):
    pilha = []
    for char in s:
        pilha.append(char)
    invertida = []
    while pilha:
        invertida.append(pilha.pop())
    return ''.join(invertida)

# Exemplo de uso
entrada = input("digite a palavra: ")
saida = reverseString(entrada)
print(f"Entrada: {entrada}")
print(f"Saída: {saida}")
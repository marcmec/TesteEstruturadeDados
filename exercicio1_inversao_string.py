def inversaoString(palavra):
    pilha = list(palavra)
    inversa = ""
    for char in pilha:
        inversa = char + inversa
        #print(inversa)
    
    print(inversa)

palavra = input("Digite uma palavra: ")

inversaoString(palavra)

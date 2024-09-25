def pilha_invert(pilha):
    lista1 = list(pilha)
    pilha_invertida = []
    palavra_invertida = ""
    for i in lista1:
        pilha_invertida.insert(0,i)

    for elemento in pilha_invertida:
        palavra_invertida += elemento

    print(palavra_invertida)


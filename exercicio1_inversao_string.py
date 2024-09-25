class Inversão:

    def inverter(palavra):
        pilha = []

        for letra in palavra:
            pilha.append(letra)

        palavra_invertida = ''

        while pilha:
            palavra_invertida += pilha.pop()

        return palavra_invertida


entrada = "Thiago Lucas *+-/"
saida = Inversão.inverter(entrada)  
print(saida)

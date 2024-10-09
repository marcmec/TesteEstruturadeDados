'''
2 fila simulação
entrada** [] (enfileirar '1', '2', desinfileirar)
saida '1'
'''

class Fila:
        def __init__(self):
            self.itens = []
            self.desisfileirar = []

        def inserir(self, novoValor):
            self.itens.append(novoValor)

        def desinfileirar(self):
            self.desinfileirar.append(self.itens.pop(0))

        def printar(self):
            if(self.itens == []):
                print(f"esta vazia a lista: {self.itens}")
            else:
                print(self.desinfileirar)

fila = Fila()                                
fila.inserir(1)
fila.inserir(2)
fila.desinfileirar()
fila.printar()
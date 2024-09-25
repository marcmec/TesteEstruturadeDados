''' 
### 2. Fila: Simulação
**Entrada:** `[]` (enfileirar `1`, `2`, desenfileirar)  
**Saída:** `1`  
'''

class Fila:
    def __init__(self):
        self.itens = []
        self.desinfileirado = []

    def inserir(self,novoValor):
        self.itens.append(novoValor)

    def estaVazia(self):
        if(self.itens == []):
            print(f"esta vazia a lista: {self.itens}")    

    def desinfileirar(self):
        self.desinfileirado.append(self.itens.pop(0))
    
    def printar(self):
        print(self.desinfileirado)

fila = Fila()
#fila.inserir(1)
#fila.inserir(2)
#fila.printar()
#fila.desinfileirar()
#fila.printar()
fila.estaVazia()
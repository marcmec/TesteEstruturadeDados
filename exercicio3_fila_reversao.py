'''### 3. Fila: Reversão
**Entrada:** `1, 2, 3`  
**Saída:** `3, 2, 1` 
''' 
class Fila:
    def __init__(self):
        self.itens = []


    def inserir(self,novoValor):
        self.itens.append(novoValor)

    def estaVazia(self):
        if(self.itens == []):
            print(f"esta vazia a lista: {self.itens}")    

    def desinfileirar(self):
        self.desinfileirado.append(self.itens.pop(0))

    def inverter(self):
        self.itens = self.itens[::-1]    
        return self.itens
    def printar(self):
        print(self.itens)

fila = Fila()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)    
fila.inverter()
fila.printar()
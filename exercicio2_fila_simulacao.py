class Fila:
    def __init__(self):
        self.fila = []

    def esta_vazio(self):
        if len(self.fila) == 0:
            return True
        else:
            return False

    def enfileirar(self, elementos: list):
        if len(elementos) == 0:
            print("A lista passada como parâmetro está vazia")
            return None
        
        for elemento in elementos:
            self.fila.append(elemento)

    def desenfileirar(self):
        if self.esta_vazio():
            return None
        
        print(self.fila.pop(0))

    def printar_fila(self):
        if self.esta_vazio():
            return None
        else:
            print(self.fila)

teste = Fila()

teste.enfileirar([1,2,3,4,5,6,7,8,9,10])
#teste.enfileirar([])
print("")
teste.printar_fila()
print("desenfileirando 5 elementos")
for i in range(5):
    teste.desenfileirar()

print("Fila resultante")
teste.printar_fila()

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir(self, valor):
        if valor < self.valor:
            if self.esquerda is None:
                self.esquerda = Node(valor)
            else:
                self.esquerda.inserir(valor)
        else:
            if self.direita is None:
                self.direita = Node(valor)
            else:
                self.direita.inserir(valor) 

    def remover(self, valorProcurado):
        if valorProcurado < self.valor:
            if self.esquerda:
                self.esquerda = self.esquerda.remover(valorProcurado)
            else:
                print(f"O valor {valorProcurado} não existe na árvore.")
        elif valorProcurado > self.valor:
            if self.direita:
                self.direita = self.direita.remover(valorProcurado)
            else:
                print(f"O valor {valorProcurado} não existe na árvore.")
        else:  # valorProcurado == self.valor
            # Caso 1: No com dois filhos
            if self.esquerda and self.direita:
                sucessor = self.direita.encontrar_minimo()
                self.valor = sucessor.valor
                self.direita = self.direita.remover(sucessor.valor)
            # Caso 2: No com apenas um filho
            elif self.esquerda:
                return self.esquerda
            elif self.direita:
                return self.direita
            else:
                return None  # No folha

        return self
    
    def encontrar_minimo(self):
        if self.esquerda:
            return self.esquerda.encontrar_minimo()
        return self

    def em_ordem(self):
        elementos = []
        if self.esquerda:
            elementos += self.esquerda.em_ordem()
        elementos.append(self.valor)
        if self.direita:
            elementos += self.direita.em_ordem()
        return elementos

    def pre_ordem(self):
        elementos = []
        elementos.append(self.valor)
        if self.esquerda:
            elementos += self.esquerda.pre_ordem()
        if self.direita:
            elementos += self.direita.pre_ordem()
        return elementos

    def pos_ordem(self):
        elementos = []
        if self.esquerda:
            elementos += self.esquerda.pos_ordem()
        if self.direita:
            elementos += self.direita.pos_ordem()
        elementos.append(self.valor)
        return elementos

    def buscar(self, valor):
        if self.valor == valor:
            return True
        if valor < self.valor:
            if self.esquerda is None:
                return None
            return self.esquerda.buscar(valor)
        else:
            if self.direita is None:
                return None
            return self.direita.buscar(valor)
        


lista = [10, 5, 15, 3 ,7 ,12 , 18]


root = Node(lista[0])


for i in range(1, len(lista)):
    root.inserir(lista[i])


print("Árvore em ordem:", root.em_ordem())
print("Árvore em pré-ordem:", root.pre_ordem())
print("Árvore em pós-ordem:", root.pos_ordem())

# Removendo um valor existente
root = root.remover(5)
print("\nÁrvore após remover 5 (em ordem):", root.em_ordem())
class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, nome):
        if isinstance(nome, str):
            nome = nome[::-1]
        self.itens.append(nome)
        return nome
    
    def desempilhar(self):
        if len(self.itens) == 0:
            return None
        else:
            self.itens.pop()
        

if __name__ == "__main__":

    pilha = Pilha()

    print(pilha.empilhar("Hello"))
    


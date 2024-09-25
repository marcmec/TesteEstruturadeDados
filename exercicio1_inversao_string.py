class Pilha:

    def __init__(self):
        self.items = []
    
    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.estaVazia():
            self.items.pop()

    def estaVazia(self):
        return len(self.items) == 0

    def reverterString(self, string):
        if isinstance(string, str):
            string = string[::-1]
        self.items.append(string)
        return string


if __name__ == "__main__":

    pilha = Pilha()

    print("Após a inversão")

    pilha.reverterString("Hello")

    print(pilha.items)


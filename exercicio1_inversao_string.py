class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def invert_string(input_string):
    stack = Stack()
    
    for char in input_string:
        stack.push(char)
    
    inverted_string = ""
    
    while not stack.is_empty():
        inverted_string += stack.pop()
    
    return inverted_string

input_string = "Prova Estrutura de Dados Avançado"
output = invert_string(input_string)
print(output)
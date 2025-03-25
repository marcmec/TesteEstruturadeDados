class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
def reverse_string(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_str = ""

    while not stack.isEmpty():
        reversed_str += stack.pop()

    return reversed_str

input_Marcos = "Hello"
output_Marcos = reverse_string(input_Marcos)
print(f"A palavra ao contrario é: {output_Marcos}")
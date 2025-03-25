def reverse_str(text):
    stack = []
    inv_text = ""
    for char in text:
        stack.append(char)
    while stack:
        inv_text += stack.pop()
    return inv_text

str_input = input("Digite uma palavra: ")

print(f"Entrada: {str_input}")
print(f"Saída: {reverse_str(str_input)}")

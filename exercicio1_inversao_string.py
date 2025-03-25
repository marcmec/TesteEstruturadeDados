
entrada = "Hello"

def invertString(value: str):
    length = len(value)
    newValue = "";
    for i in range(length-1, -1, -1):
        newValue += value[i]
    return newValue

saida = invertString(entrada)
print(saida)

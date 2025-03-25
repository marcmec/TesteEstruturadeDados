from collections import deque

def reverseFila():

    entrada = input("Digite os elementos da fila separados por vírgula (ex: a,2,hello,42): ")
    
    elementos = []
    for item in entrada.split(','):
        item = item.strip()  
        if item.isdigit(): 
            elementos.append(int(item))
        else:
            elementos.append(item)  
    
    fila = deque(elementos)
    print(f"\nFila original: {list(fila)}")

    pilha = []
    while fila:
        pilha.append(fila.popleft())
    while pilha:
        fila.append(pilha.pop())
    
    print(f"Fila revertida: {list(fila)}")
    return list(fila)

if __name__ == "__main__":
    reverseFila()
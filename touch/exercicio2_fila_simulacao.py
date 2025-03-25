from collections import deque

def simulateFila(operacoes):
    fila = deque()
    for op in operacoes:
        if op == 'enfileirar':
            fila.append(1)
            fila.append(2)
        elif op == 'desenfileirar':
            return fila.popleft() if fila else None
    return None

# Exemplo de uso
operacoes = ['enfileirar', 'desenfileirar']
saida = simulateFila(operacoes)
print(f"Operações: {operacoes}")
print(f"Saída: {saida}")
from collections import deque

def fila_simulacao():
    fila = deque()
    fila.append(1)
    fila.append(2)
    return fila.popleft()
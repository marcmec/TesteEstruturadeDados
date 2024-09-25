def encontrar_filhos(raiz, valor):
    no_encontrado = _encontrar_no(raiz, valor)
    if no_encontrado:
        resultado = []
        percurso_pre_ordem(no_encontrado, resultado)
        return resultado[1:] 

def _encontrar_no(no_atual, valor):
    if no_atual is None:
        return None

    if no_atual.valor == valor:
        return no_atual

    filho_esquerdo = _encontrar_no(no_atual.filho_esquerdo, valor)
    if filho_esquerdo:
        return filho_esquerdo

    return _encontrar_no(no_atual.filho_direito, valor)

def percurso_pre_ordem(no_atual, resultado):
    if no_atual is None:
        return

    resultado.append(no_atual.valor)
    if no_atual.filho_esquerdo:
        percurso_pre_ordem(no_atual.filho_esquerdo, resultado)
    if no_atual.filho_direito:
        percurso_pre_ordem(no_atual.filho_direito, resultado)

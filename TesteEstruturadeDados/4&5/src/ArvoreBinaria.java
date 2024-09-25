class No {
    int valor;
    No esquerda, direita;

    public No(int valor) {
        this.valor = valor;
    }
}

public class ArvoreBinaria {
    private No raiz;

    public void inserir(int valor) {
        raiz = inserirRecursivo(raiz, valor);
    }

    private No inserirRecursivo(No nodo, int valor) {
        if (nodo == null) return new No(valor);
        if (valor < nodo.valor) {
            nodo.esquerda = inserirRecursivo(nodo.esquerda, valor);
        } else if (valor > nodo.valor) {
            nodo.direita = inserirRecursivo(nodo.direita, valor);
        }
        return nodo;
    }

    public void mostrarEmOrdem() {
        mostrarEmOrdemRecursivo(raiz);
        System.out.println();
    }

    private void mostrarEmOrdemRecursivo(No nodo) {
        if (nodo != null) {
            mostrarEmOrdemRecursivo(nodo.esquerda);
            System.out.print(nodo.valor + " ");
            mostrarEmOrdemRecursivo(nodo.direita);
        }
    }

    public void mostrarFilhos(int valor) {
        No nodo = encontrarNo(raiz, valor);
        if (nodo != null) {
            System.out.print("Filhos de " + valor + ": ");
            if (nodo.esquerda != null) System.out.print(nodo.esquerda.valor + " ");
            if (nodo.direita != null) System.out.print(nodo.direita.valor + " ");
            if (nodo.esquerda == null && nodo.direita == null) {
                System.out.println("Nenhum filho.");
            } else {
                System.out.println();
            }
        } else {
            System.out.println("Nó " + valor + " não encontrado.");
        }
    }

    private No encontrarNo(No nodo, int valor) {
        if (nodo == null || nodo.valor == valor) return nodo;
        return valor < nodo.valor ? encontrarNo(nodo.esquerda, valor) : encontrarNo(nodo.direita, valor);
    }

    public static void main(String[] args) {
        ArvoreBinaria arvore = new ArvoreBinaria();
        arvore.inserir(10);
        arvore.inserir(5);
        arvore.inserir(15);
        arvore.inserir(2);
        arvore.inserir(8);

        System.out.print("Elementos em ordem: ");
        arvore.mostrarEmOrdem();

        arvore.mostrarFilhos(10);
        arvore.mostrarFilhos(5);
        arvore.mostrarFilhos(15);
        arvore.mostrarFilhos(37);
    }
}
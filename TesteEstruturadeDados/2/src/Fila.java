public class Fila {
    private int[] fila;
    private int capacidadepilha, frente, tras, tamanho;

    public Fila(int capacidadepilha) {
        this.capacidadepilha = capacidadepilha;
        fila = new int[capacidadepilha];
    }

    public void enfileirar(int item) {
        if (tamanho < capacidadepilha) {
            tras = (tras + 1) % capacidadepilha;
            fila[tras] = item;
            tamanho++;
        } else {
            System.out.println("Fila cheia!");
        }
    }

    public Integer desenfileirar() {
        if (tamanho > 0) {
            int item = fila[frente];
            frente = (frente + 1) % capacidadepilha;
            tamanho--;
            return item;
        } else {
            System.out.println("Fila vazia!");
            return null;
        }
    }

    public boolean vazia() {
        return tamanho == 0;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < tamanho; i++) {
            sb.append(fila[(frente + i) % capacidadepilha]);
            if (i < tamanho - 1) sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        Fila fila = new Fila(5);
        fila.enfileirar(3);
        fila.enfileirar(4);
        System.out.println("Fila: " + fila);
        System.out.println("Desenfileirado: " + fila.desenfileirar());
        System.out.println("Fila desfelinderada: " + fila);
    }
}

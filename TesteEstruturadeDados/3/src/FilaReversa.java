public class FilaReversa {
    private int[] fila;
    private int capacidade;
    private int tamanho;

    public FilaReversa(int cap) {
        this.capacidade = cap;
        fila = new int[cap];
        tamanho = 0;
    }

    public void enfileirar(int item) {
        if (tamanho < capacidade) {
            fila[tamanho++] = item;
        } else {
            System.out.println("Fila cheia!");
        }
    }

    public void mostrarReversa() {
        for (int i = tamanho - 1; i >= 0; i--) {
            System.out.print(fila[i] + (i > 0 ? ", " : ""));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        FilaReversa fila = new FilaReversa(5);
        fila.enfileirar(1);
        fila.enfileirar(2);
        fila.enfileirar(3);

        System.out.print("Saída: ");
        fila.mostrarReversa();
    }
}
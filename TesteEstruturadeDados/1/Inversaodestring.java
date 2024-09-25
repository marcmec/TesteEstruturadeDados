
//1° Questão

//1. Pilha: Inversão de String
//Entrada: "Hello"
//Saída: "olleH"

public class Inversaodestring {
    public static void main(String[] args) {
        String enrtada = "junior miranda";
        String saida = interveraSTR(enrtada);
        System.out.print("entrada: " + enrtada);
        System.out.print("Saída: " + saida);
    }

    public static String interveraSTR(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}
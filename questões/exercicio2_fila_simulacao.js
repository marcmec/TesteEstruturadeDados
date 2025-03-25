// Não entendi muito bem como era para ser a "entrada", então eu coloquei 
// o que tinha literalmente no GitHub. 
// Em compensação, criei o "exexicio2(1) que faz o que tem aqui só que de forma interativa"

const fila = [];

const entrada = "[] (enfileirar 1, 2, desenfileirar)";

const operacoes = entrada
  .slice(entrada.indexOf("(") + 1, entrada.indexOf(")"))
  .split(", ");

console.log(`Entrada: ${entrada}`);

for (const operacao of operacoes) {
  if (operacao.startsWith("enfileirar")) {
    const numeros = operacao.split(" ").slice(1).map(Number);
    fila.push(...numeros);
  } else if (operacao === "desenfileirar") {
    if (fila.length > 0) {
      console.log(`Saída: ${fila.shift()}`);
    } else {
      console.log(`Saída: null`);
    }
  }
}

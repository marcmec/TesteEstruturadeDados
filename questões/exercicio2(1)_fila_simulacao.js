// Criei esse aqui para colocar valores manualmente de uma forma interativa.
// Utilizando node e a biblioteca npm com prompt-sync

const prompt = require('prompt-sync')();

const quantidade = prompt("Quantas vezes deseja mexer na fila? ");

function Operacao() {
  let palavra = prompt("O que deseja fazer? (enfileirar) ou (desenfileirar): ");

  while (palavra !== "enfileirar" && palavra !== "desenfileirar") {
    console.log(`Não é possível realizar um "${palavra}". Verifique a digitação.`);
    palavra = prompt("O que deseja fazer? (enfileirar) ou (desenfileirar): ");
  }

  return palavra;
}

function enfileirar(fila) {
  const numero = prompt("Informe o número que deseja adicionar à fila: ");
  fila.push(numero);
  console.log(fila);
}

function desenfileirar(fila) {
  if (fila.length > 0) {
    fila.pop(); 
    console.log(fila);
  } else {
    console.log("Fila vazia. Não é possível desenfileirar.");
  }
}

function Fila(quantidade) {
  const fila = [];

  for (let i = 0; i < quantidade; i++) {
    const palavra = Operacao();

    if (palavra === "enfileirar") {
      enfileirar(fila);
    } else if (palavra === "desenfileirar") {
      desenfileirar(fila);
    }
  }
}

Fila(quantidade);
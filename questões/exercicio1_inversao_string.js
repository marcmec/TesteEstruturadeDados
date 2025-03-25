const prompt = require('prompt-sync')();

const palavra = prompt("Informe a palavra que deseja inverter: ")

const pilha = [];
let vazia = " ";

for (let i = 0; i < palavra.length; i++) {
    pilha.push(palavra[i]);
}

while (pilha.length > 0) {
    vazia += pilha.pop();
}


console.log(vazia);
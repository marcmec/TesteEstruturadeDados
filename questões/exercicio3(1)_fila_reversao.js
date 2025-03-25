// Aqui eu também decidi colocar de uma forma mais interativa
// Utilizando node e a biblioteca npm com prompt-sync

const prompt = require('prompt-sync')();


function Numero () {
    const array = prompt("Informe o tamanho do array: ")
    const numeros = [];

    for (let i = 0; i < array; i++) {
        const numero = prompt(`Informe o numero ${i+1}: `)
        numeros.push(numero)
    }

    console.log(`Array Original`) 
    console.log(numeros);

    return numeros;

}

function Inverter (original) {
    const invertida = [];

    for (let i = original.length - 1; i >= 0; i--) {
        invertida.push(original[i]);
    }

    console.log(`Array Novo`)
    console.log(invertida);
}

const original = Numero();
Inverter(original);
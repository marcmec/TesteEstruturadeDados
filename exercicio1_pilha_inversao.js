class Pilha {
  constructor() {
    this.items = {}
    this.count = 0;
  }
  
  push(item) {
    this.items[this.count] = item;
    this.count++
  }
  
  read() {
    let item = this.items[0];
    for (let i = 1; i < this.count; i++) {
      item = this.items[i] + item
    }
    return item
  }
}

class InverterString {
  constructor(texto) {
    this.texto = texto;
  }
  
  exec() {
    const arr = this.texto.split("");
    const pilha = new Pilha();
    for (let item of arr) {
      pilha.push(item)
    }
    return pilha.read()
  }
}

const teste = new InverterString("Hello");

console.log(teste.exec())
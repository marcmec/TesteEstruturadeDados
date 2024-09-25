class Fila {
  constructor() {
    this.items = {}
    this.count = 0;
    this.lowestCount = 0;
  }
  
  enfilerar(valor) {
    this.items[this.count] = valor;
    this.count++;
  }
  
   desinfilerar() {
        if (this.count === 0) {
            return undefined;
        }
        const itemDel = this.items[this.lowestCount];
        delete this.items[this.lowestCount];
        this.lowestCount++;
        return itemDel
    }
    
  reverter()  {
    let item = `${this.items[this.count - 1]}`
    for (let i = this.count - 2; i >= this.lowestCount; i--) {
      item += `${this.items[i]}`
    }
    return item
  }
}

const fila = new Fila();

fila.enfilerar(1);
fila.enfilerar(2);
fila.enfilerar(3);
fila.enfilerar(4);
fila.enfilerar(5);


console.log(fila.reverter());


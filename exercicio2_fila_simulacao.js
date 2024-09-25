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
    
}

const fila = new Fila();

fila.enfilerar(1);
fila.enfilerar(2);

console.log(fila.desinfilerar());


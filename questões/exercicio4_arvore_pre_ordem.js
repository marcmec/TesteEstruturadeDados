// Aqui eu também decidi criar uma árvore mais interativa, onde você coloca
// os valores no terminal.
// Utilizando node e a biblioteca npm com prompt-sync

const prompt = require('prompt-sync')();

const quantidade = parseInt(prompt("Quantos numeros deseja por na árvore? "));

for (let i = 0; i < quantidade; i++) {
    const numero = parseInt(prompt(`Informe o ${i+1}º número: `))
    tree.insert(numero)
}

class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(data) {
        const newNode = new Node(data);

        if (this.root === null) {
            this.root = newNode;

        } else {
            this.insertNode(this.root, newNode)
        }
    }

    insertNode(node, newNode) {
        if (newNode.data < node.data) {
            if (node.left === null) {
                node.left = newNode;

            } else {
                this.insertNode(node.left, newNode)
            }
        } else {
            if (node.right === null) {
                node.right = newNode;

            } else {
                this.insertNode(node.right, newNode)
            }
        }
    }

    preorder(node = this.root) {
        if (node !== null) {
            console.log(node.data);
            this.preorder(node.left);
            this.preorder(node.right);
        }
    }

    inorder(node = this.root) {
        if (node !== null) {
            this.inorder(node.left);
            console.log(node.data);
            this.inorder(node.right);
        }
    }

    postorder(node = this.root) {
        if (node !== null) {
            this.postorder(node.left);
            this.postorder(node.right);
            console.log(node.data)
        }
    }

}

const tree = new BinaryTree();

console.log("Árvore em pré-ordem:");
tree.preorder();

console.log("Árvore em ordem:");
tree.inorder();

console.log("Árvore em pos-ordem:");
tree.postorder();
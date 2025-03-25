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
      this.nodeMap = {}; 
    }
  
    insert(data) {
      const newNode = new Node(data);
      this.nodeMap[data] = newNode; 
  
      if (this.root === null) {
        this.root = newNode;
      } else {
        this.insertNode(this.root, newNode);
      }
    }
  
    insertNode(node, newNode) {
      if (newNode.data < node.data) {
        if (node.left === null) {
          node.left = newNode;
        } else {
          this.insertNode(node.left, newNode);
        }
      } else {
        if (node.right === null) {
          node.right = newNode;
        } else {
          this.insertNode(node.right, newNode)
        }
      }
    }
  
    findChildren(value) {
      const node = this.findNode(value); 
      if (!node) return [];
  
      const children = [];
      if (node.left) children.push(node.left.data)
      if (node.right) children.push(node.right.data)
  
      return children;
    }
  
    findNode(value) {
      return this.nodeMap[value] || null; 
    }
  }
  
  const tree = new BinaryTree();
  const valores = [10, 5, 15];
  valores.forEach(num => tree.insert(num));
  
  const searchValue = 10;
  const filhos = tree.findChildren(searchValue);
  
  console.log(valores)
  console.log(filhos)
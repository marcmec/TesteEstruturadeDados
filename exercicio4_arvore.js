class Node {
  constructor(valor) {
    this.valor = valor;
    this.right = null;
    this.left = null;
  }
}


class BinarySearchTree {
  constructor() {
    this.root = undefined;
  }
  insert(valor) {
    if (this.root == null) {
      this.root = new Node(valor);
    } else {
      this.insertNode(this.root, valor);
    }
  }
  insertNode(node, valor) {
    if (valor < node.valor) {
      if (node.left == null) {
        node.left = new Node(valor);
      } else {
        this.insertNode(node.left, valor);
      }
    } else if (node.right == null) {
      node.right = new Node(valor);
    } else {
      this.insertNode(node.right, valor);
    }
  }
  getRoot() {
    return this.root;
  }
  search(valor) {
    return this.searchNode(this.root, valor);
  }
  searchNode(node, valor) {
    if (node == null) {
      return false;
    }
    if (valor < node.valor) {
      return this.searchNode(node.left, valor);
    } else if (valor > node.valor) {
      return this.searchNode(node.right, valor);
    }
    return true;
  }
  inOrderTraverse(callback) {
    this.inOrderTraverseNode(this.root, callback);
  }
  inOrderTraverseNode(node, callback) {
    if (node != null) {
      this.inOrderTraverseNode(node.left, callback);
      callback(node.valor);
      this.inOrderTraverseNode(node.right, callback);
    }
  }
  preOrderTraverse(callback) {
    this.preOrderTraverseNode(this.root, callback);
  }
  preOrderTraverseNode(node, callback) {
    if (node != null) {
      callback(node.valor);
      this.preOrderTraverseNode(node.left, callback);
      this.preOrderTraverseNode(node.right, callback);
    }
  }
  postOrderTraverse(callback) {
    this.postOrderTraverseNode(this.root, callback);
  }
  postOrderTraverseNode(node, callback) {
    if (node != null) {
      this.postOrderTraverseNode(node.left, callback);
      this.postOrderTraverseNode(node.right, callback);
      callback(node.valor);
    }
  }
  min() {
    return this.minNode(this.root);
  }
  minNode(node) {
    let current = node;
    while (current != null && current.left != null) {
      current = current.left;
    }
    return current;
  }
  max() {
    return this.maxNode(this.root);
  }
  maxNode(node) {
    let current = node;
    while (current != null && current.right != null) {
      current = current.right;
    }
    return current;
  }
  remove(valor) {
    this.root = this.removeNode(this.root, valor);
  }
  removeNode(node, valor) {
    if (node == null) {
      return undefined;
    }
    if (valor < node.valor) {
      node.left = this.removeNode(node.left, valor);
      return node;
    } else if (valor > node.valor) {
      node.right = this.removeNode(node.right, valor);
      return node;
    }
    if (node.left == null && node.right == null) {
      node = undefined;
      return node;
    }
    if (node.left == null) {
      node = node.right;
      return node;
    } else if (node.right == null) {
      node = node.left;
      return node;
    }
    const aux = this.minNode(node.right);
    node.valor = aux.valor;
    node.right = this.removeNode(node.right, aux.valor);
    return node;
  }
}

const bst = new BinarySearchTree();

bst.insert(10);
bst.insert(15);
bst.insert(25);

const callback = (value) => console.log(value)

bst.inOrderTraverse(callback)

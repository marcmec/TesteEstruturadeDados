class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    def get_children(self):
        children = []
        if self.left:
            children.append(self.left.value)
        if self.right:
            children.append(self.right.value)
        return children


tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)

print(f"Os filhos da raiz são (esquerda, direita): {tree.get_children()}")

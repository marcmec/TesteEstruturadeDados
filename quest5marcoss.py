class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def get_children(self, value):
        node = self._find_node(self.root, value)
        if node:
            children = []
            if node.left:
                children.append(node.left.value)
            if node.right:
                children.append(node.right.value)
            return children
        return None

    def _find_node(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._find_node(node.left, value)
        return self._find_node(node.right, value)

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.get_children(10))
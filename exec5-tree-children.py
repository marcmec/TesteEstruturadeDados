class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.is_root = True

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            node.is_root = False
            while True:
                parent = current
                if node.value < current.value:
                    current = current.left
                    if current == None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current == None:
                        parent.right = node
                        return

    def pre_order(self, node):
        if node != None:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)


    def children_pre_order(self, node):
        if node != None:
            if node.is_root == False:
                print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

tree = BinaryTree()

numbers_input = input("Insira os números (separado por vírgula e espaço): ")

for i in numbers_input.split(", "):
    tree.insert(int(i))

tree.children_pre_order(tree.root)
print()

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

    def pre_order(self):
        print(self.value, end=" ") 
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()



tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(25)
tree.insert(35)
tree.pre_order()
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def putLeft(self, node):
        self.left = node

    def putRight(self, node):
        self.right = node
class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self) -> None:
    self.root = None

  def add(self, val):
    added = self._add(val, self.root)
    if not self.root:
      self.root = added

  def _add(self, val, node):
    if not node:
      return Node(val)
    
    if val <= node.val:
      node.left = self._add(val, node.left)
    else:
      node.right = self._add(val, node.right)
    return node
  
  def inorder(self):
    print("inorder:", end=" ")
    self._inorder(self.root)
    print()

  def _inorder(self, node):
    if not node:
      return
    
    self._inorder(node.left)
    print(node.val, end=" ")
    self._inorder(node.right)

  def preorder(self):
    print("preorder:", end=" ")
    self._preorder(self.root)
    print()

  def _preorder(self, node):
    if not node:
      return
    
    print(node.val, end=" ")
    self._preorder(node.left)
    self._preorder(node.right)

bt = BinaryTree()
bt.add(50)
bt.add(70)
bt.add(35)
bt.add(22)
bt.add(21)
bt.add(23)
bt.add(36)
bt.add(37)

bt.preorder()
bt.inorder()
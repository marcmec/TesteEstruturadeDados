from BinaryTree import BinaryTree

def find_childrens(root, val):
  if (node := _find_childrens(root, val)):
    output = []
    pre_order(node, output)
    return output[1:]


def _find_childrens(node, val):
  if not node:
    return None
  
  if node.val == val:
    return node
  
  return _find_childrens(node.left, val) or _find_childrens(node.right, val)

def pre_order(node, output):
  if not node:
    return
  
  output.append(node.val)
  pre_order(node.left, output)
  pre_order(node.right, output)

bt = BinaryTree()

bt.add(50)
bt.add(70)
bt.add(35)
bt.add(22)
bt.add(21)
bt.add(23)
bt.add(36)
bt.add(37)

print(find_childrens(bt.root, 35))
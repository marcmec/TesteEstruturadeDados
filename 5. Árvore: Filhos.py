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
  
  return _find_childrens(node.left) or _find_childrens(node.right)

def pre_order(node, output):
  if not node:
    return
  
  output.append(node.val)
  pre_order(node.left)
  pre_order(node.right)


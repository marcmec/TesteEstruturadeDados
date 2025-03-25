from Node import Node

def pre_order(node: Node):
    if(node == None):
        return
    
    if(node.left != None):
        print(node.left.value)

    if(node.right != None):
        print(node.right.value)

    pre_order(node.left)
    pre_order(node.right)

node01 = Node(10)
node02 = Node(5)
node03 = Node(12)
node04 = Node(23)
node05 = Node(41)
node06 = Node(35)
node07 = Node(67)
node08 = Node(8)
node09 = Node(22)

node01.putLeft(node02)
node01.putRight(node03)
node02.putLeft(node04)
node02.putRight(node05)
node03.putLeft(node06)
node03.putRight(node07)
node04.putLeft(node08)
node04.putRight(node09)

pre_order(node01)
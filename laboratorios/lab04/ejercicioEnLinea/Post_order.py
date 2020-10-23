"""
Estructura de datos y algoritmos 1
Laboratorio 4
Punto 2.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014
"""

class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree(object):
    def insert(self, root, node):
        if root is None:
            return node
        if root.value < node.value:
            root.right = self.insert(root.right, node)
        else:
            root.left = self.insert(root.left, node)
        return root


    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.left)
            self.post_order_place(root.right)
            print (root.value)

def post_order(node_order):
  List = Node(node_order[0])
  node = BinarySearchTree()
  for nd in node_order:
      node.insert(List, Node(nd))
  print ("------Post order ---------")
  node.post_order_place(List)


print(post_order([50,30,24,5,28,45,98,52,60]))
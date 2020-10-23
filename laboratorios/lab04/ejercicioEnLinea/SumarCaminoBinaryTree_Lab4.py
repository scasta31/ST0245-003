"""
Estructura de datos y algoritmos 1
Laboratorio 4
Punto 2.2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __iter__(self):
        return self.root.__iter__()
    
    def insert_aux(self, value, node):
        if node == None:
            node = TreeNode(value)
            return node
        if value < node.value:
            node.left = BinarySearchTree.insert_aux(self, value, node.left)
        elif value > node.value:
            node.right = BinarySearchTree.insert_aux(self, value, node.right)
        return node
            
    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            BinarySearchTree.insert_aux(self, value, self.root)
            
    def search_aux(self, value, node):
        if node == None:
            print("Not found")
            return False
        elif node.value == value:
            print("Found")
            return True
        
        if node.value > value:
            return BinarySearchTree.search_aux(self, value, node.left)
        elif node.value < value:
            return BinarySearchTree.search_aux(self, value, node.right)
        else:
            return False
        
    def search(self, value):
        BinarySearchTree.search_aux(self, value, self.root)
        
    def sumaElCamino(self,a,suma):
        a=TreeNode(a)
        if (a == None):
            return False
        if (a.left == None and a.right == None):
            return suma == a
        else:
            return (BinarySearchTree.sumaElCamino(self,a.left, suma-a) or BinarySearchTree.sumaElCamino(self,a.right,suma-a)) 
        
class TreeNode:
    
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None
        

arbol = BinarySearchTree()
arbol.insert(5)
arbol.insert(4)
arbol.insert(8)

print(arbol.sumaElCamino(arbol.root,9))
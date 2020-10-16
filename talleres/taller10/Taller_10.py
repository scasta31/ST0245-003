#!/usr/bin/env python
# coding: utf-8

# In[47]:


"""
Estructura de datos y algoritmos 1
Taller 10
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __iter__(self):
        return self.root.__iter__()
    
    def insert_aux(self, pair, node):
        if node == None:
            node = TreeNode(pair)
            return node
        if pair[1] < node.value[1]:
            node.left =  self.insert_aux(self, pair, node.left)
        elif pair[1] > node.value[1]:
            node.right = self.insert_aux(self, pair, node.right)
        return node
            
    def insert(self, pair):
        if self.root == None:
            self.root = TreeNode(pair)
        else:
            self.insert_aux(self, pair, self.root)
            
    def search_aux(self, pair, node):
        if node == None:
            print("Not found")
            return False
        elif node.value[1] == pair[1]:
            print("Found")
            return True
        
        if node.value[1] > pair[1]:
            return search_aux(self, pair, node.left)
        elif node.value[1] < pair[1]:
            return search_aux(self, pair, node.right)
        else:
            return False
        
    def search(self, pair):
        self.search_aux(self, pair, self.root)
        
class TreeNode:
    
    def __init__(self, pair, left = None, right = None):
        self.value =pair
        self.left = None
        self.right = None 
        
arbol = BinarySearchTree()
persona1=["Diana",3158756548]
arbol.insert(persona1)
print(arbol.root.value)


# Cálculo de la complejidad
""" Para insertar, se parte de que el nodo esta balanceado y el codigo
se pregunta si el nodo en el que esta es menor que el elemento que quiero
insertar, por ende, va reduciendo N a la mitad en cada subnivel de decisión

Por tanto,

T(n) = T(n/2) + T(n/4) + T(n/8) + T(n/16) ... T(n/(2^n))

Resolviendo, la complejidad es:
O(log(n))

"""  
  

  


# In[ ]:





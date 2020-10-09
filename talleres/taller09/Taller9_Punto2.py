"""
Estructura de datos y algoritmos 1
Taller 9 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def get(self):
		return str(self)

class HashTable:
	
	def __init__(self):
		self.capacity = 50
		self.size = 0
		self.buckets = [None]*self.capacity

	def hash(self, key):
		hashsum = 0
		for index, c in enumerate(key):
			hashsum += (index + len(key)) ** ord(c)
			hashsum = hashsum % self.capacity
		return hashsum

	def insert(self, key, value):
		self.size += 1
		index = self.hash(key)
		node = self.buckets[index]
		if node is None:
			self.buckets[index] = Node(key, value)
			return
		prev = node
		while node is not None:
			prev = node
			node = node.next
		prev.next = Node(key, value)

	def find(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return None
		else:
			return node.value

H=HashTable()

H.insert("Google","Estados Unidos")
H.insert("La Locura","Colombia")
H.insert("Nokia","Finlandia")
H.insert("Sony","Japon")


print("La empresa Nokia esta ubicada en",H.find("Nokia"))
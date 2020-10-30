
"""
Taller 12 Puntos 1 y 2
Estructura datos y algoritmos 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillon Sepulveda 201610035014
"""

from collections import defaultdict 

class GraphAl: 

  def __init__(self, vertices): 
    self.V= vertices 
    self.graph = defaultdict(list) 
    self.adjList = [[] for _ in range(vertices)]

  def addArc(self,source,destination): 
        self.graph[source].append(destination) 
       
  def find_path_BFS(self, source, destination): 
  
        visited =[False]*(self.V) 
        temp=[] 
        temp.append(source) 
        visited[source] = True
        while temp: 
            n = temp.pop(0) 
            if n == destination: 
              return True
            for i in self.graph[n]: 
                if visited[i] == False: 
                    temp.append(i) 
                    visited[i] = True
        return 
        
  def find_path_DFS(self, source, destination):
      
      temp=[] 
      visited =[False]*(self.V)
      visited[source] = True
      temp.append(source)
      if source == destination:
          return True
      for i in self.adjList[source]:
          if not visited[i]:
            if GraphAl.find_path_DFS(self, i, destination):
                return True
      temp.pop()
      return False
   
g= GraphAl(4)
g.addArc(0, 1) 
g.addArc(0, 2) 
g.addArc(1, 2) 
g.addArc(2, 0) 
g.addArc(2, 3) 
g.addArc(3, 3) 
  
print(g.find_path_BFS(1,3))
print(g.find_path_DFS(3,3))

# Nos apoyamos en los codigos de geekforgeeks para entender el problema y copiar parte del # codigo
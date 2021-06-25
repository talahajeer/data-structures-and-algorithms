from collections import deque
class Vertex:
  def __init__(self,value):
    self.value = value

class Edge:
  def __init__(self,vertex, weight =0):
    self.vertex = vertex
    self.weight = weight

class Graph:

  def __init__(self):
    self.adjacencyList = {}

  def add_vertex(self,vertex):
    self.adjacencyList[vertex] =[]
    return self.adjacencyList.get(vertex)

  def add_edge(self,strat_v, end_v, weight =0):
    if not strat_v in self.adjacencyList or  not end_v in self.adjacencyList:
      raise Exception('No existing start or end vertix')
    
    edge = Edge(end_v, weight)
    self.adjacencyList[strat_v].append(edge)
    return self.adjacencyList.get(strat_v)
  
  def get_vertices(self):
    if not len(self.adjacencyList):
        raise Exception('No vertices found')

    collection = []
    for k in self.adjacencyList.keys():
      collection.append(k.value)
    return collection


  def get_unique_vertices(self):
    if not self.size():
         raise Exception('No vertices found')

    collection = set()
    for key in self.adjacencyList.keys():
      collection.add(key.value)

    return collection


  def get_neighbors(self,vertex):
      result = []
      if len(self.adjacencyList.get(vertex)):

          for l in range(len(self.adjacencyList.get(vertex))):
            result.append([self.adjacencyList.get(vertex)[l].vertex.value,self.adjacencyList.get(vertex)[l].weight])
      
      return result


  def size(self):
    return len(self.adjacencyList)



if __name__ == "__main__":
  g =  Graph()
  zero =  Vertex(0)
  one =  Vertex(1)
  two =  Vertex(2)
  twoToo =  Vertex(2)
  three =  Vertex(3)
  four =  Vertex(4)
  fourToo =  Vertex(4)
  five =  Vertex(5)

  g.add_vertex(zero)
  g.add_vertex(one)
  g.add_vertex(two)
  g.add_vertex(twoToo)
  g.add_vertex(three)
  g.add_vertex(four)
  g.add_vertex(fourToo)
  print(g.add_vertex(five))

  g.add_edge(zero, two, 3)
  g.add_edge(two, three)
  g.add_edge(two, four)
  g.add_edge(three, five)
  g.add_edge(four, five)
from collections import deque
# from stacks_and_queues.stacks_and_queues import *
class Vertex:
  def __init__(self,value):
    self.value = value

class Edge:
  def __init__(self,vertex, weight =0):
    self.vertex = vertex
    self.weight = weight

class Queue():

    def __init__(self) -> None:

        self.dq = deque()

    def enqueue(self, value):

        self.dq.appendleft(value)

    def dequeue(self):

        return self.dq.pop()

    def __len__(self):

        return len(self.dq)

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

  
  def __str__(self) :
    if self.adjacencyList:
      result = ''
      for v in self.adjacencyList:
          result += f"{v}:{self.get_neighbors(v)}, "
      return result
    else:
      return 'null'

  def get_children(self, vertex):
    return self.adjacencyList.get(vertex, [])

  def breadth_first_search(self, start_vertex, action=(lambda x: None)):
    queue = Queue()
    visited = set()
    output = []
    
    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    while len(queue):
      current_vertex = queue.dequeue()
      # action(current_vertex)
      output.append(current_vertex)
      neighbors = self.get_children(current_vertex)

      for edge in neighbors:
        neighbor_vertex = edge.vertex

        if neighbor_vertex in visited:
          continue
        else:
          visited.add(neighbor_vertex)
        queue.enqueue(neighbor_vertex)
    return output



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
  
  g.breadth_first_search(zero, lambda v: print(v.value))
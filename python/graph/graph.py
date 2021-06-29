from collections import deque
from stacks_and_queues.stacks_and_queues import *
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


  def business_trip(self,city_names):
    available_trip = False
    total_trip = 0
    # vertices = self.get_vertices() # [all city names]
    # print("get neighbors",road_trip)
    for city in city_names:
      if not available_trip:
        road_trip = self.get_neighbors(city_names.index(city)) # [[cityname,edgewight],....]
        for road in road_trip:
          if city_names[1] in road: 
            available_trip = True
            total_trip +=road[1]
            print("total trip",total_trip)
            break
      else:
        return [False,0]
    print([available_trip,total_trip])
    return [available_trip,total_trip]


  def depth_first(self, v):
    vertices = []
    stack = Stack()
    stack.push(v)
    visited = []
    while not stack.is_empty():
      top_vertex = stack.pop()
      vertices.append(top_vertex)

      top_vertex_neighbors = self.get_neighbors(top_vertex)

      for neighbor in top_vertex_neighbors:
        if  not neighbor[0] in visited:
          stack.push(neighbor[0])
          visited.append(neighbor[0])
    return vertices
    




if __name__ == "__main__":
  g =  Graph()
  Pandora =  Vertex("Pandora")
  Narnia =  Vertex("Narnia")
  Metroville =  Vertex("Metroville")
  Arendelle =  Vertex("Arendelle")
  New_Monstropolis =  Vertex("New_Monstropolis")
  Naboo =  Vertex("Naboo")

  g.add_vertex(Pandora)
  g.add_vertex(Narnia)
  g.add_vertex(Metroville)
  g.add_vertex(Arendelle)
  g.add_vertex(New_Monstropolis)
  g.add_vertex(Naboo)

  g.add_edge(Pandora, Metroville, 82)
  g.add_edge(Pandora, Arendelle,150)
  g.add_edge(Narnia, Metroville,37)
  g.add_edge(Narnia, Naboo,250)
  g.add_edge(Arendelle, Metroville,99)
  g.add_edge(Arendelle, New_Monstropolis,42)
  g.add_edge(Naboo, Metroville,26)
  g.add_edge(Naboo, New_Monstropolis,73)
  g.add_edge(Metroville, New_Monstropolis,105)

  print(g.business_trip([Naboo, Pandora]))

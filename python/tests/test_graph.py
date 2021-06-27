from graph.graph import *
import pytest

def test_add_vertex():
    g =  Graph()
    zero =  Vertex(0)
    actual = g.add_vertex(zero)
    expected =[]
    assert actual == expected


def test_add_edge():
    g =  Graph()
    zero =  Vertex(0)
    one =  Vertex(1)
    g.add_vertex(zero)
    g.add_vertex(one)
    actual = g.add_edge(one, zero, 3)[0].weight
    expected = 3
    assert actual == expected

def test_add_nodes(test_):
    actual = test_.get_unique_vertices()
    expected = {0, 1, 2, 3, 4, 5}
    assert actual == expected


def test_get_nighbors():
    g =  Graph()
    zero =  Vertex(0)
    one =  Vertex(1)
    two =  Vertex(2)
    g.add_vertex(zero)
    g.add_vertex(one)
    g.add_vertex(two)
    g.add_edge(zero, two, 3)
    g.add_edge(zero, one)
    actual = g.get_neighbors(zero)
    expected = [[2,3],[1,0]]
    assert actual == expected

def test_size(test_):
    actual = test_.size()
    expected = 8
    assert actual == expected


def test_get_nighbors_one_node():
    g =  Graph()
    zero =  Vertex(0)
    g.add_vertex(zero)
    g.add_edge(zero, zero, 3)
    actual = g.get_neighbors(zero)
    expected = [[0,3]]
    assert actual == expected

def test_breadth_first_search(test_):
    actual = test_.breadth_first_search(2)
    expected = [2, 3]
    assert actual == expected

    test_.add_edge(five,one)
    actual2 = test_.breadth_first_search(2)
    expected2 = [2, 4, 1, 3]
    assert actual2 == expected2

    actual3 = test_.breadth_first_search('8')
    expected3 = 'value does not exist'
    assert actual3 == expected3


@pytest.fixture
def test_():
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
  g.add_vertex(five)

  g.add_edge(zero, two, 3)
  g.add_edge(two, three)
  g.add_edge(two, four)
  g.add_edge(three, five)
  g.add_edge(four, five)

  return g


#   g.add_node('A')
#     g.add_node('B')
#     g.add_node('C')
#     g.add_node('D')

#     g.add_edge('A','B',9)
#     g.add_edge('A','C')
#     g.add_edge('B','D')
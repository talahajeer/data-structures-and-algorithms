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


def test_business_trip(graph):
    cities_lists =[['Jordan', 'Syria', 'Turkey'],['Turkey','KSA','Jordan'],['Iraq', 'Syria'],['KSA','Turkey']]
    actual = [business_trip(graph, cities) for cities in cities_lists]
    expected = [(True,'$60'),(False,'$0'),(True,'$25'),(False,'$0')]
    assert actual == expected

    
def test_breadth_first_search():
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

    g.add_edge(one, two, 3)
    g.add_edge(one, three)
    g.add_edge(one, four)
    g.add_edge(three, five)
    g.add_edge(four, five)
    actual = []
    x = g.breadth_first_search(one)
    for v in x:
        actual.append(v.value)
    expected = [1, 2, 3, 4, 5]
    assert expected == actual


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
  return g
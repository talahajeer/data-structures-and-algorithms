from tree.tree import *
import pytest
def test_init_empty():
    binary_tree = BinaryTree()
    actual = binary_tree.__str__()
    expected = 'None'
    assert actual == expected

def test_init_one():
 node1 = TNode(1)
 binary_tree = BinaryTree(node1) 
 actual = binary_tree.__str__()
 expected = '1'
 assert actual == expected


def test_init_right_and_left():
 node1 = TNode(1)
 node1.left = TNode(2)
 node1.right = TNode(3)
 binary_tree = BinaryTree(node1) 
 actual = [binary_tree.root.value , binary_tree.root.left.value , binary_tree.root.right.value]
 expected = [1,2,3]
 assert actual == expected 

def test_pre_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.pre_order()]
 expected = [[1, 2, 3, 4, 5]]
 assert actual == expected 

def test_in_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.in_order()]
 expected = [[2, 1, 4, 3, 5]]
 assert actual == expected 

def test_post_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.post_order()]
 expected = [[2, 4, 5, 3, 1]]
 assert actual == expected 

def test_max_value(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = binary_tree.find_maximum_value()
 expected = 5
 assert actual == expected  

def test_max_value_empty(tree_test):
    binary_tree = BinaryTree() 
    actual = binary_tree.find_maximum_value()
    expected = 'No tree found'
    assert actual == expected 

def test_breadth_first(tree_bread):
    actual = tree_bread.bread_first()
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected


def test_add_in_BST():
    obj = BinarySearchTree()
    bst_node = TNode(50)
    bst_node = obj.add(20)
    bst_node = obj.add(10)
    bst_node = obj.add(30)
    bst_node = obj.add(40)

    actual = obj.in_order([bst_node])
    expected = [None, 10, 20, 30, 40]
    assert actual == expected

def test_contains(tree_test):
    obj = BinarySearchTree()
    bst_node = TNode(50)
    bst_node = obj.add(20)
    bst_node = obj.add(10)
    bst_node = obj.add(30)
    bst_node = obj.add(40)
    actual = [obj.contains(0,bst_node) , obj.contains(20,bst_node) , obj.contains(10,bst_node), obj.contains(1,bst_node)]
    expected = [False, True, True, False]
    assert actual == expected 

def test_k_array(node1_test):
  k_tree = K_tree(node1_test)
  actual = k_tree.FizzBuzzTree()
  expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
  assert actual == expected    

@pytest.fixture
def tree_test():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(4)
    node1.right.right = TNode(5)
    return node1


@pytest.fixture
def tree_bread():
    node1 = TNode(2)
    node1.left = TNode(7)
    node1.left.right = TNode(6)
    node1.left.right.left = TNode(5)
    node1.left.right.right = TNode(11)
    node1.left.left = TNode(2)
    node1.right = TNode(5)
    node1.right.right = TNode(9)
    node1.right.right.left = TNode(4)
    binary_tree = BinaryTree(node1)
    return binary_tree         

@pytest.fixture
def node1_test():
  node1 = KNode(1)
  node1.children.append(KNode(2))
  node1.children.append(KNode(3))
  node1.children.append(KNode(4))
  node1.children[0].children.append(KNode(5))
  node1.children[1].children.append(KNode(6))
  node1.children[1].children.append(KNode(7))
  node1.children[2].children.append(KNode(8))
  node1.children[2].children.append(KNode(9))
  node1.children[2].children.append(KNode(10))
  return node1    
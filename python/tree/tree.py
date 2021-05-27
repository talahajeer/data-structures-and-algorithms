# import pysnooper

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, node=None):
    self.top = node
  
  def push(self, value):
    if not self.top:
        self.top = Node(value)
    else:
        node = Node(value)
        node.next = self.top
        self.top = node

  # @pysnooper.snoop()
  def pop(self):
    if not self.is_empty():
      temp_node = self.top
      self.top = self.top.next
      temp_node.next = None
      return temp_node.value
    raise Exception("Cannot pop an empty Stack")
  
  def is_empty(self):
    return not self.top

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, root=None):
    self.root = root
    self.pre_list_values = []
    self.in_list_values = []
    self.post_list_values = []

  def pre_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):
      self.pre_list_values.append(root.value)

      if root.left:
        walk(root.left)
      
      if root.right:
        walk(root.right)
         
    walk(self.root)
    return self.pre_list_values
    
  def in_order(self):
    """ in-order traversal of our tree """
    def walk(root):

        if root.left:
            walk(root.left)
        
        self.in_list_values.append(root.value)
        
        if root.right:
            walk(root.right)
            
    walk(self.root)
    return self.in_list_values

  def post_order(self):
    """ post-order traversal of our tree """
    def walk(root):

        if root.left:
            walk(root.left)
        
        if root.right:
            walk(root.right)
            
        self.post_list_values.append(root.value)

    walk(self.root)  
    return self.post_list_values
  
  
  
  def bread_first(self):
     # Use queque for FIFO
     pass

class BinarySearchTree():
    def __init__(self,root=None):
        self.root = root
 

    def add(self,value,tree):

        if tree.root.value == None:
            tree.root = TNode(value)
        else:
            if tree.root.value == value:
                return "Value already exists in the tree"
            if value < tree.root.value:
                if tree.root.left:
                    print(tree.root.value,"in less check",value)
                    tree.root.left = self.add(value,tree.root.left)  
            else:
                if tree.root.right:
                    print(tree.root.value,"in greater check",value)
                    tree.root.right = self.add(value,tree.root.right) 
        return BinaryTree.pre_order(tree)

    def contains(self,value):
        if value == self.root:
            return True

        if value < self.root:
            if self.left == None:
                return False
            return self.left.contains(value)

        if self.right == None:
            return False
        return self.right.contains(value)

                        



if __name__ == "__main__":
  node1 = TNode(1)
  node1.left = TNode(2)
  node1.right = TNode(3)
  node1.right.left = TNode(4)
  node1.right.right = TNode(5)

  binary_tree = BinaryTree(node1)
  print(binary_tree.pre_order())
  print(binary_tree.in_order())
  print(binary_tree.post_order())


  Binary_Search_Tree = BinarySearchTree()
#   new_tree = Binary_Search_Tree.add(6,binary_tree)
#   print(Binary_Search_Tree.add(6,Binary_Node))
#   print(new_tree)
#   print(binary_tree.pre_order())
  print(Binary_Search_Tree.contains(1))


   



# Think about
class KNode:
  def __init__(self, value=None):
    self.value = value
    # How could you implement this for k of any size?
    self.children = []

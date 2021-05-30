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

  def __str__(self):
      if self.root:
        return f"{self.root.value}"  
      return f"{self.root}"

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
  
  
  def find_maximum_value(self):
      """ find the maximum value """
      if self.root is not None:
          self.maximum_value = self.root.value
          def walk(root):
            if root.left:
              walk(root.left)

            if self.maximum_value < root.value:
              self.maximum_value = root.value
              
            if root.right:
              walk(root.right)
              
          walk(self.root)
          return self.maximum_value
      else:
        return 'No tree found'  

  def bread_first(self):
     # Use queque for FIFO
     pass

class BinarySearchTree():
  def __init__(self,value=None):
    self.node = TNode(value)

  def add(self,value):
    # new_node = Node(value)
    if self.node.value == None:
      self.node.value = value
    else:
      if value == self.node.value:
        return 'value already exists'
      
      if value < self.node.value:
        if self.node.left:
          self.node.left.add(value)
        else:
          self.node.left = BinarySearchTree(value)
      else:
        if self.node.right:
          self.node.right.add(value)
        else:
          self.node.right = BinarySearchTree(value)

  def in_order(self, list = []):
    if (self.node.left):
      self.node.left.in_order(list)
    list.append(self.node.value)
    if (self.node.right):
      self.node.right.in_order(list)
    return list

  def contains(self,value,parent= None):
    if value == self.node.value:
      return True
    if (value < self.node.value):
      if (self.node.left):
        return self.node.left.contains(value, self.node)
      else:
        return False
    else:
      if (self.node.right):
        return  self.node.right.contains(value, self.node)
      else:
        return False

                        



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
  print(binary_tree.find_maximum_value())
  

  bsTree = BinarySearchTree()
  bsTree.add(5)
  bsTree.add(4)
  bsTree.add(3)
  bsTree.add(2)
  bsTree.add(1)
  bsTree.add(6)
  bsTree.add(0)
  print(bsTree.contains(3),bsTree.contains(13))
  print(bsTree.in_order())


   



# Think about
class KNode:
  def __init__(self, value=None):
    self.value = value
    # How could you implement this for k of any size?
    self.children = []

class EmptyStackException(Exception):
  pass



class Node: 
  def __init__(self, value=None):
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
  
  def pop(self):
      if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
      raise EmptyStackException("Cannot pop from an empty stack")
  
  def is_empty(self):
    """ Returns True if Empty and false otherwise """
    if self.top:
      return False
    return True

  def peek(self):
    """ Returns the value at the top without modifying the stack, raises an exception otherwise """
    if not self.is_empty():
      return self.top.value
    
    raise EmptyStackException("Cannot peek an empty stack")
  
  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####
class PseudoQueue:
  def __init__(self, node=None):
    self.stack = Stack()
    self.reversed_stack = Stack()
  
  def enqueue(self, value):
      self.stack.push(value)

  
  def dequeue(self):
      if not self.stack.is_empty():
        while not self.stack.is_empty():
            popped = self.stack.pop()
            self.reversed_stack.push(popped)
    
        result = self.reversed_stack.pop()
        if self.stack.is_empty():
            while not self.reversed_stack.is_empty():
                 self.stack.push(self.reversed_stack.pop())
        return result
      else:
            raise EmptyStackException("Cannot pop from an empty stack") 
  def peek(self):
    """ Returns the value at the top without modifying the queue, raises an exception otherwise """
    if not self.stack.is_empty():
        current = self.stack.top
        items = []
        while current:
            items.insert(0,str(current.value))
            current = current.next
        return items[0]
    
    raise EmptyStackException("Cannot peek an empty stack")
  def __str__(self):
    current = self.stack.top
    items = []
    while current:
      items.insert(0,str(current.value))
      current = current.next
    return "\n".join(items) 
pseudoQueue = PseudoQueue()
pseudoQueue.enqueue(1)
pseudoQueue.enqueue(2)
pseudoQueue.enqueue(3)
pseudoQueue.dequeue()
print(pseudoQueue.peek())

print(pseudoQueue)
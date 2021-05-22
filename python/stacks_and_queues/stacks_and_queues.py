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
    if self.top:
        current = self.top
        self.top = self.top.next
        return current.value
    else:
        raise EmptyStackException("Cannot pop an empty stack")

  def peek(self):
    if not self.is_empty():
      return self.top.value
    raise EmptyStackException("Cannot peek an empty stack")

  def is_empty(self):
    if self.top:
      return False
    return True

  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)

class Queue:
  def __init__(self,value=None):
    self.front = None
    self.rear = None
    self.value = value
    self.next = None

  def enqueue(self, value):
    node = Node(value)
    if not self.front:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = self.rear.next

  def dequeue(self):
    if self.front:
      current = self.front
      self.front = current.next
      return current.value
    else: 
      raise EmptyStackException("Cannot dequeue an empty queue")
   
  def peek(self):
    if self.front:
      return self.front.value
    raise EmptyStackException("Cannot peek an empty queue")    

  def is_empty(self):
    if self.front:
      return False
    return True  

  def __str__(self):
    current = self.front
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return " =>> ".join(items)

if __name__ == "__main__":
  stack = Stack()
#   print(stack)
#   print(stack.peek())
  stack.push(5)
#   print(stack)
  stack.push(4)
  print(stack)
  print(stack.peek())
  print(stack)

  queue = Queue()
  print(queue)
  queue.enqueue(3)
  print(queue)
  queue.enqueue(4)
  print(queue)
  queue.enqueue(5)
  print(queue)
  queue.dequeue()
  print(queue)
  print(queue.is_empty())
class Node:
  def __init__(self, data=None):
      self.data = data
      self.next = None
  
  def __str__(self):
      return f"{self.data}"
   


class Linked_list:
  def __init__(self):
    self.head = None

  def insert (self, data=None):
    new_node = Node(data)
    if self.head :
      new_node.next = self.head
    self.head = new_node

  def includes(self,value):
    current = self.head 
    is_include = False
    while (current):
        if current.data == value :
            is_include = True
        current = current.next
    return is_include
      

  def __str__(self):
    """ Returns a string representaiton of the linked list
        1 -> 3 -> 4 -> Null
    """
    output = ""

    current = self.head
    while current:
      output += "{%s} -> " %(current.data,)
      current = current.next
    output += " NULL"
    return output
  


if __name__ == "__main__":
  linked = Linked_list()
  linked.insert("Muhannad")
  linked.insert("Manar")
  linked.insert(10)
#   print(linked)
#   print(linked.includes(55),linked.includes("Manar"),linked.includes(5))
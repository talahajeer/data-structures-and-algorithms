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

  def append(self,value):
      node = Node(value)
      current = self.head
      while current.next :
        current=current.next
      current.next =node


  def insertAfter(self ,value, newVal) :
    node=Node(newVal)
    if self.head is None:
      self.head = node
    else:
      current = self.head
      while current.next:
        if current.data==value:
          bef_val=current.next
          current.next =node
          node.next=bef_val
          return node.data
        current=current.next

  def insertBefore(self, value, newVal):
      current = self.head
      if current.data == value:
          new_node = Node(newVal)
          new_node.next = current
          self.head = new_node
      else:
          while (current.next):
              if current.next.data == value:
                  new_node = Node(newVal)
                  new_node.next = current.next
                  current.next = new_node
                  break
              current = current.next  

  def includes(self,value):
    current = self.head 
    is_include = False
    while (current):
        if current.data == value :
            is_include = True
        current = current.next
    return is_include
      
  def kthFromEnd(self, k):
        try:
          n = -1
          current = self.head
          while current:
            current = current.next
            n = n + 1
          if n >= k:
            current = self.head
            for i in range(n - k):
              current = current.next
          return current.data
        except:
          return "no value found"

  def __str__(self):
    
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
  linked.append("Adel")
  linked.insertAfter(10,"Tala")
  linked.insertBefore("Tala","One")
  zzz = linked.zipLists([1,2,3])
  print(zzz)
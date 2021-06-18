from  linked_list.linked_list import *


class Hashmap:
    """
    this is obviously a hashmap class
    """

    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        index = (sum *19)% self.size
        return index

    def __str__(self):
        output = []

        for i in self.map:
            if i:
                current = i.head
                while current:
                    output.append(' -> '.join(current.data))
                    current = current.next
        string_hash = ' ,'.join(output)
        return string_hash



    def add(self, key, value):
       index = self.hash(key)
       if self.contains(key):
            current = self.map[index].head
            while current:
                if key == current.data[0]:
                    current.data[1] =  value
                current = current.next
                return self
       if not self.map[index]:
           self.map[index] = Linked_list()
       self.map[index].append([ key, value])
       return self.__str__()




    def get(self, key):
        index = self.hash(key)
        if self.map[index]:
            current = self.map[index].head
            while current:
                if key == current.data[0]:
                    return current.data[1]
                current = current.next
        return "not found"



    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            current = self.map[index].head
            while current:
                if key == current.data[0]:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    hash_map = Hashmap()
    hash_map.add('Nour','She is studing remotely')
    hash_map.add('Tala','She feels lazy all day')
    hash_map.add('alaT','She feels lazy all day')

    hash_map.add('Manar','She participates in class')
    # print(hash_map.get('Noura'))
    print(hash_map)

    print('pass')
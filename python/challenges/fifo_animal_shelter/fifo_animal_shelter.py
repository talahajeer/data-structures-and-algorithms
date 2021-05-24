class EmptyQueueException(Exception):
    pass
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        if self.front:
            return False
        return True
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        raise EmptyQueueException("Cannot dequeue an empty queue")
    def peek(self):
        if not self.is_empty():
            return self.front.value
        raise EmptyQueueException("Cannot peek an empty queue")
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)


class Cat:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "cat"


class Dog:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "dog"


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
    def enqueue(self, pet):
        if pet.type == "cat":
            self.cat.enqueue(pet.name)
        elif pet.type == "dog":
            self.dog.enqueue(pet.name)
        else:
            return "only cats and dogs"
    def dequeue(self, pref):
        if pref == "cat":
            self.cat.dequeue()
        elif pref == "dog":
            self.dog.dequeue()
        else:
            return "only cats and dogs"


if __name__ == "__main__":
    dog1 = Dog("bobi")
    dog2 = Dog("sasi")
    dog3 = Dog("soso")
    dog4 = Dog("lulu")
    cat1 = Cat("kitty")
    cat2 = Cat("lucy")
    cat3 = Cat("sabi")
    cat4 = Cat("radi")
    animal_sh = AnimalShelter()
    animal_sh.enqueue(dog2)
    animal_sh.enqueue(cat1)
    animal_sh.enqueue(cat2)
    animal_sh.enqueue(cat3)
    print(animal_sh.cat)
    print("--------------")
    animal_sh.dequeue("cat")
    print(animal_sh.cat)
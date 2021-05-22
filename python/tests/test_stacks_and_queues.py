from stacks_and_queues.stacks_and_queues import *
import pytest

def test_push_stack():
    stack = Stack()
    for i in range(1,5):
        stack.push(i)
    stack.push(5)
    assert stack.top.value == 5

def test_pop_stack():
    stack = Stack()
    for i in range(1,5):
        stack.push(i)
    assert stack.pop() == 4

def test_peek_stack():
    stack = Stack()
    for i in range(1,5):
        stack.push(i)
    assert stack.peek() == 4

def test_is_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

# --------------------------------------------------------------------
def test_enqueue():
    queue = Queue()
    assert queue.front == None
    queue.enqueue(5)
    assert queue.front.value == 5
    queue.enqueue(6)
    assert queue.rear.value == 6

def test_dequeue():
    queue = Queue()
    for i in range(1,5):
        queue.enqueue(i)
    assert queue.dequeue() == 1
    assert queue.front.value == 2

def test_peek_queue():
    queue = Queue()
    for i in range(1,5):
        queue.enqueue(i)
    assert queue.peek() == 1
    queue.dequeue()
    assert queue.peek() == 2
  
def test_is_empty_queue():
    queue = Queue()
    assert queue.is_empty() == True
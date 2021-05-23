from challenges.queue_with_stacks.queue_with_stacks import *
import pytest

def test_enqueue(queue_test):
    excpected = "one\ntwo\nthree"
    actual = f"{queue_test}"
    assert excpected == actual

def test_enqueue_to_empty():
    queue = PseudoQueue()
    queue.enqueue("one")
    excpected = "one"
    actual = f"{queue}"
    assert excpected == actual

def test_peek(queue_test):
    excpected = "one"
    actual = f"{queue_test.peek()}"
    assert excpected == actual


def test_empty_queue_peek():
    queue = PseudoQueue()
    with  pytest.raises(EmptyStackException):
        queue.peek()

def test_empty_queue_dequeue():
    queue = PseudoQueue()
    with  pytest.raises(EmptyStackException):
        queue.dequeue()

def test_dequeue(queue_test):
    queue_test.dequeue()
    excpected = "two\nthree"
    actual = f"{queue_test}"
    assert excpected == actual


def test_adding_multiple_to_queue():
    queue = PseudoQueue()
    for i in range(1,4):
        queue.enqueue(i)
    excpected = "1\n2\n3"
    actual = f"{queue}"
    assert excpected == actual

@pytest.fixture
def stack_test():
  stack = PseudoQueue()
  stack.push('one')
  stack.push("two")
  stack.push("three")
  return stack


@pytest.fixture
def queue_test():
  queue = PseudoQueue()
  queue.enqueue("one")
  queue.enqueue("two")
  queue.enqueue("three")
  return queue
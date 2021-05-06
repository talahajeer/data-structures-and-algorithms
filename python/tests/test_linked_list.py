from linked_list.linked_list import *
import pytest

def test_insert(list_test):
    excpected = "{10} -> {Manar} -> {Muhannad} ->  NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    actual = [list_test.includes(55),list_test.includes("Manar"),list_test.includes(5)]
    excpected = [False, True , False]
    assert excpected == actual


@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert("Muhannad")
    linked.insert("Manar")
    linked.insert(10)
    return linked
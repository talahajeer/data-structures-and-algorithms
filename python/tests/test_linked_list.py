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

def test_append(list_test):
    excpected = "{10} -> {Manar} -> {Muhannad} -> {Adel} ->  NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_insertAfter(list_test):
    actual = f"{list_test}"
    excpected = "{10} -> {Tala} -> {Manar} -> {Muhannad} ->  NULL"
    assert excpected == actual

def test_insertBefore(list_test):
    actual = f"{list_test}"
    excpected = "{10} -> {One} -> {Tala} -> {Manar} -> {Muhannad} ->  NULL"
    assert excpected == actual

@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert("Muhannad")
    linked.insert("Manar")
    linked.insert(10)
    linked.append("Adel")
    linked.insertAfter(10,"Tala")
    linked.insertBefore("Tala","One")
    return linked
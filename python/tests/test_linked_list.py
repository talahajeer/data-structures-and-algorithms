from linked_list.linked_list import *
import pytest

def test_insert(list_test_insert):
    excpected = "{10} -> {Manar} -> {Muhannad} ->  NULL"
    actual = f"{list_test_insert}"
    assert excpected == actual

def test_includes(list_test_insert):
    actual = [list_test_insert.includes(55),list_test_insert.includes("Manar"),list_test_insert.includes(5)]
    excpected = [False, True , False]
    assert excpected == actual

def test_append(list_test_append):
    excpected = "{10} -> {Manar} -> {Muhannad} -> {Adel} ->  NULL"
    actual = f"{list_test_append}"
    assert excpected == actual

def test_insertAfter(list_test_insertAfter):
    actual = f"{list_test_insertAfter}"
    excpected = "{10} -> {Tala} -> {Manar} -> {Muhannad} ->  NULL"
    assert excpected == actual

def test_insertBefore(list_test_insertBefore):
    actual = f"{list_test_insertBefore}"
    excpected = "{10} -> {One} -> {Tala} -> {Manar} -> {Muhannad} ->  NULL"
    assert excpected == actual

def test_kthFromEnd(list_test_insert):
    actual_output1 =list_test_insert.kthFromEnd(2)
    actual_output2=list_test_insert.kthFromEnd(0)
    actual_output3 =list_test_insert.kthFromEnd(10)
    expected_output1 = 10
    expected_output2 = 1
    expected_output3 = "Sorry invalid input"
    assert actual_output1 == expected_output1
    assert actual_output2 == expected_output2
    assert actual_output3 == expected_output3


@pytest.fixture
def list_test_insert():
    linked = Linked_list()
    linked.insert("Muhannad")
    linked.insert("Manar")
    linked.insert(10)
    return linked

@pytest.fixture
def list_test_append():
    linked = Linked_list()
    linked.append("Adel")  
    return linked

@pytest.fixture
def list_test_insertAfter():
    linked = Linked_list()
    linked.insertAfter(10,"Tala")
    return linked    

@pytest.fixture
def list_test_insertBefore():
    linked = Linked_list()
    linked.insertBefore("Tala","One")    
    return linked      
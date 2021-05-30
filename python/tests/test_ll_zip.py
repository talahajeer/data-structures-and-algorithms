import pytest
from linked_list.linked_list import *
from challenges.ll_zip.ll_zip import zipLists

def test_zipLists(list1,list2):
    actual = zipLists(list1,list2)
    expected = '{1} -> {5} -> {3} -> {9} -> {2} -> {4} ->  NULL'
    assert actual == expected

def test_zipLists2(list2):
    list1 = Linked_list()
    list1.append(1)
    list1.append(3)
    actual = zipLists(list1,list2)
    expected = '{1} -> {5} -> {3} -> {9} -> {4} ->  NULL'
    assert actual == expected

def test_zipLists3(list1):
    list2 = Linked_list()
    list2.append(5)
    list2.append(9)
    actual = zipLists(list1,list2)
    expected = '{1} -> {5} -> {3} -> {9} -> {2} ->  NULL'
    assert actual == expected

@pytest.fixture
def list1():
    list1 = Linked_list()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    return list1


    
@pytest.fixture
def list2():
    list2 = Linked_list()
    list2.append(5)
    list2.append(9)
    list2.append(4)
    return list2
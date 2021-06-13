from challenges.insertion_sort.blog import *

def test_arr():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort([8,4,23,42,16,15])
    assert expected == actual

def test_empty_arr():
    expected = []
    actual = insertion_sort([])
    assert expected == actual      
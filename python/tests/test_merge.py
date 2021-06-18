from challenges.merge_sort.merge_sort import *

def test_sort():
    input = [8,4,23,42,16,15]
    actual = merge_sort(input)
    expected = [4, 8, 15, 16, 23, 42]# , [-2, 5, 8, 12, 18, 20] , [5, 5, 5, 7, 7, 12] , [2, 3, 5, 7, 11, 13]]
    assert actual == expected
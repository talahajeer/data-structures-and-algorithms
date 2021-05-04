from challenges.array_binary_search.array_binary_search import BinarySearch

def test_BinarySearch():
    excepted = 2
    actual = BinarySearch([4,8,15,16,23,42],15)
    assert actual == excepted

def test_BinarySearch2():
    excepted = -1
    actual = BinarySearch([11,22,33,44,55,66,77],90)
    assert actual == excepted

def test_BinarySearch3():
    excepted = -1
    actual = BinarySearch([1, 2, 3, 5, 6, 7], 4)
    assert actual == excepted
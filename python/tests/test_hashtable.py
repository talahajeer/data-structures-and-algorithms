from hashtable.hashtable import *

def test_add():
    hash_map = Hashmap()
    expexted = 'Nour -> She is studing remotely'
    actual = hash_map.add('Nour','She is studing remotely')
    assert expexted == actual

def test_add_duplicate():
    hash_map1 = Hashmap()
    hash_map1.add('Manar','She is studying all day')
    hash_map1.add('Manar','She participates in class')
    actual = hash_map1.__str__()
    expected = 'Manar -> She participates in class'
    assert  actual == expected


def test_hashmap_get():
    hash_map = Hashmap()
    hash_map.add('Nour','She is studing remotely')
    hash_map.add('Tala','She feels lazy all day')
    hash_map.add('Manar','She participates in class')
    input = ['Nour','Tala', 'Manar']
    expected = ['She is studing remotely','She feels lazy all day','She participates in class']
    actual = [hash_map.get(key) for key in input]
    assert expected == actual

def test_hashmap_contains():
    hash_map = Hashmap()
    hash_map.add('Nour','She is studing remotely')
    hash_map.add('Tala','She feels lazy all day')
    hash_map.add('Manar','She participates in class')
    input = ['Nour','Tala', 'Manar','Raneem']
    expected = [True, True, True, False]
    actual = [hash_map.contains(key) for key in input]
    assert expected == actual
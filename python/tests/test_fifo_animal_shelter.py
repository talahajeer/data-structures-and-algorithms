from challenges.fifo_animal_shelter.fifo_animal_shelter import Cat,Dog,AnimalShelter,EmptyQueueException
import pytest
def test_cat_enqueue():
    expected = "kitty"
    cat1=Cat('kitty')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(cat1)
    actual = f"{animal_sh.cat}"
    assert actual == expected
def test_dog_enqueue():
    expected = "Bobi"
    dog1=Dog('Bobi')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(dog1)
    actual = f"{animal_sh.dog}"
    assert actual == expected
def test_queue__cat_multiple_enqueue(queue_cat_test):
    expected = "kitty lucy sabi radi"
    actual = f"{queue_cat_test}"
    assert actual == expected
def test_queue__dog_multiple_enqueue(queue_dog_test):
    expected = "bobi sasi soso lulu"
    actual = f"{queue_dog_test}"
    assert actual == expected
def test_queue_cat_dequeue(queue_cat_test):
    expected = 'kitty'
    actual = queue_cat_test.dequeue()
    assert actual == expected
def test_queue_dog_dequeue(queue_dog_test):
    expected = 'bobi'
    actual = queue_dog_test.dequeue()
    assert actual == expected
def test_queue_cat_multiple_dequeue(queue_cat_test):
    for num in range(4):
        queue_cat_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_cat_test.dequeue()
def test_queue_dog_multiple_dequeue(queue_dog_test):
    for num in range(4):
        queue_dog_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_dog_test.dequeue()
@pytest.fixture
def queue_cat_test():
    cat1=Cat('kitty')
    cat2=Cat('lucy')
    cat3=Cat('sabi')
    cat4=Cat('radi')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(cat1)
    animal_sh.enqueue(cat2)
    animal_sh.enqueue(cat3)
    animal_sh.enqueue(cat4)
    return animal_sh.cat
@pytest.fixture
def queue_dog_test():
    dog1=Dog('bobi')
    dog2=Dog('sasi')
    dog3=Dog('soso')
    dog4=Dog('lulu')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(dog1)
    animal_sh.enqueue(dog2)
    animal_sh.enqueue(dog3)
    animal_sh.enqueue(dog4)
    return animal_sh.dog
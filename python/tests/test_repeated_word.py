from challenges.repeated_word.repeated_word import *
import pytest

def test_first_repeated():
    string = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(string)
    expected = 'a'
    assert actual == expected


def test_first_repeated_empty():
    string = ""
    actual = repeated_word(string)
    expected = "No Repetition"
    assert actual == expected

def test_first_repeated_no_repeat():
    string = "My name is Tala"
    actual = repeated_word(string)
    expected = "No Repetition"
    assert actual == expected
from challenges.left_join.left_join import *

def test_left_join():

    hash1 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outift': 'garb',
        'guide': 'usher',
    }
    hash2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'], 
        ['diligent', 'employed', 'idle'], 
        ['outift', 'garb', None], ['guide', 'usher', 'follow']
    ]
    actual = left_join(hash1,hash2)
    assert expected == actual


def test_empty_left():
    hash1 = {
    }

    hash2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }    
    expected = 'No left hashmap'
    actual = left_join(hash1,hash2)
    assert expected == actual


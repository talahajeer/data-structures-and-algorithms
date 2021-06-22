# from hashtable.hashtable import *

def left_join(hash1,hash2):

    if len(hash1) > 0:
        join = []
        for key in hash1:
            value1 = hash1[key]
            if key in hash2:
                value2 = hash2[key]
            else:
                value2 = None
            join.append([key,value1,value2])
        return join
    else:
        return 'No left hashmap'

if __name__=='__main__':
    h1 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outift': 'garb',
        'guide': 'usher',
    }

    h2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }
    print(left_join(h1,h2))
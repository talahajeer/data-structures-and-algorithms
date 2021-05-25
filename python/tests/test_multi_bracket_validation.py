from challenges.multi_bracket_validation.multi_bracket_validation import *
def test1():
    test_array=['{}','{}(){}','()[[Extra Characters]]','(){}[[]]','{}{Code}[Fellows]','(())','[({}]','(](','{(})','{',')','{]']
    expected=[True,True,True,True,True,True,False,False,False,False,False,False]
    actual=[multi_bracket_validation(string) for string in test_array]
    assert actual == expected
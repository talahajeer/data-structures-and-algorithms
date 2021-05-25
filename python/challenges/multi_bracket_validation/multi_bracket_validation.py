def multi_bracket_validation(input):
    opening=['(','[','{']
    closing=[')',']','}']
    # input_array=input.split("")
    # print(input_array)
    check_list = []
    for i in input:
        if i in opening:
            check_list.append(i)
        elif i in closing:
            pos = closing.index(i)
            if ((len(check_list) > 0) and
                (opening[pos] == check_list[len(check_list)-1])):
                check_list.pop()
            else:
                return  False
    if len(check_list) == 0:
        return True
    else:
        return False
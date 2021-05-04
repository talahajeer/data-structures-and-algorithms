def insertShiftArray(array,n):
    if len(array)%2 == 1:
        array.insert(int(len(array) /2)+1 , n)
    else:
        array.insert(int(len(array) /2) , n)    
    return array
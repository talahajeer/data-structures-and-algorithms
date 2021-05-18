from linked_list.linked_list import *

def zipLists(list1,list2):
    """
    zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes 
    alternate between the two lists and return a reference to the head of the zipped list. 
    """
    ll = Linked_list()
    current1 = list1.head
    current2 = list2.head
    while(current1 or current2):
        if current1:
            ll.append(current1.data)
            current1 = current1.next
        if current2:
            ll.append(current2.data)
            current2 = current2.next
    return f"{ll}"
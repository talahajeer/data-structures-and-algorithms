def BinarySearch(list, search_key):
  first_index = 0
  last_index = int(len(list)-1)
  while first_index <= last_index:
    if last_index % 2 != 0:
       last_index + 1
    mid_index= int((first_index + last_index) / 2)
    if list[mid_index] == search_key:
      return mid_index
    elif list[mid_index] < search_key:
      first_index = mid_index + 1
    else:
      last_index = mid_index - 1
  return -1

# In Collaboration with manar , Noor , Noura  
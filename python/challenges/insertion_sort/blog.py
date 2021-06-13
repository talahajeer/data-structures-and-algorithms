def insertion_sort(arr):
    for i in range(len(arr)):
        # print(i)
        j = i - 1
        temp = arr[i]

        while j>= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j- 1

        arr[j+1] = temp
    return arr

if __name__ == '__main__':
    insertion_sort([8,4,23,42,16,15])    
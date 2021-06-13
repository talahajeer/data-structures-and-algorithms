def insertion_sort(arr):
    i = 1 
    print("beforeeeeeeeeee",arr)
    for i in range(len(arr)):
        print(i)
        j = i
        temp = arr[i]

        while j>= 0 and temp < arr[j]:
            print(j)
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp
    print("afteeeeeeeeer",arr)

insertion_sort([8,4,23,42,16,15])    
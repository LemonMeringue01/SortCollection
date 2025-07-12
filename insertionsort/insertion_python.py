def InsertionSort():
    array = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input("Enter element "+ str(i+1) +" : "))
        array.append(element)

    print(array)


    for i in range(1,n):
        insertionPoint = i
        elemToCompare = array[i]
        for j in range(i-1, -1, -1):
            if array[j]>elemToCompare:
                array[j+1] = array[j]
                insertionPoint = j
        array[insertionPoint] = elemToCompare


    print(array)



InsertionSort()
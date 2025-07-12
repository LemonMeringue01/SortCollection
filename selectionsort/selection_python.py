def SelectionSort():
    array = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input("Enter element "+ str(i+1) +" : "))
        array.append(element)


    print(array)

    for i in range(n):
        CurrentMinIndex = i
        for j in range(i+1,n):
            if array[j]<array[CurrentMinIndex]:
                CurrentMinIndex = j
        if CurrentMinIndex != i:
            temp = array[i]
            array[i] = array[CurrentMinIndex]
            array[CurrentMinIndex] = temp


    print(array)

            

SelectionSort()
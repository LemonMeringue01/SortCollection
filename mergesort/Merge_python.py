def mergeSort(arr,left,right):
    if left<right:
        middle=(left+right)//2
        mergeSort(arr,left,middle)
        mergeSort(arr,middle+1,right)
        merge(arr,left,middle,right)



#from geeksforgeeks.org https://www.geeksforgeeks.org/python/python-program-for-merge-sort/
def merge(arr,left,middle,right):
    lengthLeft = middle-left+1
    lengthRight = right-middle
    leftSect =  [0]*lengthLeft
    rightSect = [0]*lengthRight

    for i in range(0, lengthLeft):
        leftSect[i] = arr[left + i]

    for j in range(0, lengthRight):
        rightSect[j] = arr[middle + 1 + j]

    i=0
    j=0
    k=left

    while i<lengthLeft and j<lengthRight:
        if leftSect[i]<=rightSect[j]:
            arr[k]=leftSect[i]
            i=i+1
            k=k+1
        else:
            arr[k] = rightSect[j]
            j=j+1
            k=k+1

    while i<lengthLeft:
        arr[k] = leftSect[i]
        i += 1
        k += 1
    
    while j<lengthRight:
        arr[k] = rightSect[j]
        j += 1
        k += 1



array = [2,6,3,2,7,4,2,1,9,5,4,8]
print(array)
mergeSort(array,0,len(array)-1)
print(array)
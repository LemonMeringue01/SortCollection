def quickSort(arr,start,end):
    if start<end:
        pivot = partition(arr, start, end)
        quickSort(arr,start, pivot-1)
        quickSort(arr, pivot+1, end)

def partition(arr, start, end):
    #lomuto partition.
    #pretty much from https://www.geeksforgeeks.org/dsa/hoares-vs-lomuto-partition-scheme-quicksort/

    pivot = arr[end]

    i = start-1
    
    for j in range(start, end):
        #do swaps to get sections in order
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

        #put pivot into place


    #made multiple errors here. remeber to watch indentation, people.
    arr[i+1],arr[end]=arr[end],arr[i+1]

    return (i+1)
    





array = [2,6,4,8,3,1,6,9,4,3]
print(array)
quickSort(array, 0, len(array)-1)
print(array)
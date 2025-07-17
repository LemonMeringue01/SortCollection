def quickSort(arr,start,end):
    if start<end:
        pivot = partition(arr, start, end)
        quickSort(start, pivot-1)
        quickSort(pivot+1, end)

def partition(arr, start, end):
    


array = [2,6,4,8,3,1,6,9,4,3]
quickSort(array, 0, len(array)-1)
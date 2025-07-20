def heapSort(arr):
    """
    take in array
    make it into heap
    for loop length of arr
        take out max/min element and insert it
        make it into a heap again
    going to use the example from slides as it's slightly easier to follow.
    that uses a max heap.

    """
    size = len(arr)
    buildMaxHeap(arr,size) #using all elems, make a maxheap

    elemsToSort = size
    for i in range(size-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]   #take the found maximum and put it to the end, decrementing as the found maximums decrease.
        elemsToSort=elemsToSort-1
        maxHeapify(arr,0,elemsToSort)



def buildMaxHeap(arr, size):
    for i in range((size//2)-1,-1,-1):
        maxHeapify(arr,i,size)

def maxHeapify(arr,root,size):
    leftChild=(2*root)+1
    rightChild=(2*root)+2

    largest = root #assume root is the largest value? for comparisons.
    if leftChild<size and arr[leftChild]>arr[root]: #if leftchild exists, within scope of array, and its value is more than the current root's:
        largest = leftChild

    if rightChild<size and arr[rightChild]>arr[largest]: #if rightchild exists, within scope, and value > the bigger value from either left or root:
        largest = rightChild
    
    if largest!=root: #if largest value is no longer considered to be root:
        arr[root],arr[largest] = arr[largest],arr[root]
        maxHeapify(arr,largest,size)



    



array = [2,6,4,8,3,1,6,9,4,3]
print(array)
heapSort(array)
print(array)

#second last one(really last though) let's go.
#will not work for input other than integer arrays
#IMPORTANT NOTE!! I keep getting for loops not working. Range(0,n) means it will include 0 index, but stop at the n-1 index. annoying.

def countingSort(arr):

    if arr==[]:
        return []

    size = len(arr)
    #find max value

    occurencesArray = [0]*(max(arr)+1)
    
    #count value occurences
    for i in range(size):
        occurencesArray[arr[i]]+=1

    #get running sum
    for i in range(1,len(occurencesArray)):
        occurencesArray[i] = occurencesArray[i]+occurencesArray[i-1]

    outputArray = [0]*size
    #assign final array using occurences array
    for i in range(size-1,-1,-1):
        outputArray[occurencesArray[arr[i]]-1] = arr[i]
        occurencesArray[arr[i]]-=1

    return outputArray
    



array = [4,6,4,4,6,4,3,5,6,5,4,6,4,6,5,3]
print(array)
print(countingSort(array))


def merge(L,R):
    #print("merge") #
    #print(L,R) #
    arr = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        #print(i, j) #
        if L[i] < R[j]:
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1
    
    if i >= len(L):
        arr.extend(R[j:])
    elif j >= len(R):
        arr.extend(L[i:])
    #print(arr) #
    return arr

def mergeSort(arr):
    #print("mergeSort") #
    if len(arr) <= 1:
        return arr
    middle = round(len(arr)/2)
    #print(middle) #
    L = mergeSort(arr[:middle])
    R = mergeSort(arr[middle:])
    return merge(L,R)
    
#print(mergeSort([]))
#print(mergeSort([1]))
print(mergeSort([5,4,3,2,1]))
print(mergeSort([3,5,37,5,1]))

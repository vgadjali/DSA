def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

# this comment is just to improve readability due to horizontal scroll!!!


def pivot(arr, start, end):
    print("pivot arr={}, start = {}, end = {}".format(arr, start, end))
    if len(arr) <=1:
        return arr
    pivot = arr[start]
    i = start + 1 #going down the line
    j = start + 1 #keeping track of last small number + 1
    while i <= end:
        if arr[i] < pivot:
            #swap i w/ j 
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1 
        else:
            i+=1 #move on to next
    
    #swap pivot with j-1
    arr[0], arr[j-1] = arr[j-1], arr[0]
    print(arr)
    
    return j-1
    
    
def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivotIndex = pivot(arr,0,len(arr)-1)
    quickSort(arr[:pivotIndex])
    quickSort(arr[pivotIndex+1:])
    print("arr = {}, pivotIndex = {}".format(arr, pivotIndex))
    return arr
    

#print(quickSort([4,2,5,3,1]))
print(quickSort([3,2,1,5,4]))
#print(quickSort([]))
#not working, can't figure out why
def mergeArr(arr1,arr2):
    
        
    sortedArr = []
    def merge(arr1, arr2):
        if arr1 == [] or arr2 == []:
            return arr1 + arr2
            
        if arr1[0] < arr2[0]:
            sortedArr.append(arr1[0])
            return merge(arr1[1:], arr2)
        else:
            sortedArr.append(arr2[0])
            return merge(arr1, arr2[1:])
      
    merge(arr1,arr2)
    return sortedArr
    
print(mergeArr([1,2],[]))
print(mergeArr([],[3,4]))
print(mergeArr([],[]))
print(mergeArr([1,3,5],[2,4,5, 8, 9]))
print(mergeArr([1,3,5],[2,4,5]))
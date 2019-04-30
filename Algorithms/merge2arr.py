def merge(arr1,arr2):
    if arr1 == [] or arr2 == []:
        return arr1 + arr2
    i = 0
    j = 0
    sortedArr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sortedArr.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            sortedArr.append(arr2[j])
            j+=1 
        else:
            sortedArr.append(arr2[j])
            sortedArr.append(arr1[i])
            i+=1 
            j+=1 
    while i<len(arr1):
        sortedArr.append(arr1[i])
        i+=1
    while j<len(arr2):
        sortedArr.append(arr2[j])
        j+=1
        
    return sortedArr
    
print(merge([1,2],[]))
print(merge([],[3,4]))
print(merge([],[]))
print(merge([1,3,5],[2,4,5, 8, 9]))
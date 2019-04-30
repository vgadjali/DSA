def insertionSort(arr):
    if len(arr) <2:
        return arr 
    i = 1 
    while i < len(arr):
        print("----")
        j = i-1 
        while j >=0:
            print("i = {}, j = {}".format(i,j))
            if arr[i] >= arr[j]:
                arr.insert(j+1, arr[i])
                arr.pop(i+1)
                break
            elif j==0:
                arr.insert(0, arr[i])
                arr.pop(i+1)
            j-=1
            print(arr)
            print("i = {}, j = {}".format(i,j))
        i+=1 
    return arr 

#print(insertionSort([5,4,3,2,1]))
#print(insertionSort(["a","c","b"]))
print(insertionSort([4,6,4,1,4,9]))
#print(insertionSort([]))
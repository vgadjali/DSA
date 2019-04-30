import math

def getDigit(num,digit):
    return math.floor(abs(num)/(10**digit)) %10
    
def countDigits(num):
    if num == 0:
        return 1 
    return math.floor(math.log(abs(num),10)) + 1

def getMaxDigits(arr):
    maxDigits = 0
    for i in arr:
        maxDigits = max(maxDigits, countDigits(i))
    return maxDigits
    
def radixSort(arr, d = 0):
    _0 = []
    _1 = []
    _2 = []
    _3 = []
    _4 = []
    _5 = []
    _6 = []
    _7 = []
    _8 = []
    _9 = []
    
    for i in arr:
        digit = getDigit(i, d)
        if digit == 0:
            _0.append(i)
        elif digit == 1:
            _1.append(i)
        elif digit == 2:
            _2.append(i)
        elif digit == 3:
            _3.append(i)
        elif digit == 4:
            _4.append(i)
        elif digit == 5:
            _5.append(i)
        elif digit == 6:
            _6.append(i)
        elif digit == 7:
            _7.append(i)
        elif digit == 8:
            _8.append(i)
        elif digit == 9:
            _9.append(i)
        
    arr = _0
    arr.extend(_1)
    arr.extend(_2)
    arr.extend(_3)
    arr.extend(_4)
    arr.extend(_5)
    arr.extend(_6)
    arr.extend(_7)
    arr.extend(_8)
    arr.extend(_9)
    d+=1
    if d > getMaxDigits(arr):
        return arr
    return radixSort(_0,d) #for loop to getMaxDigits for nonrecursive solution
    
print(radixSort([5,65,3,25,4,6,354]))
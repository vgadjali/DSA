import math

class MaxBHeap():
    def __init__(self):
        self.values = []

    def __str__(self):
        return ", ".join(str(x) for x in self.values)

    def insert(self,value):
        self.values.append(value)
        self.bubbleUp()
        return True

    def bubbleUp(self):
        def parent(i):
            return math.floor((i-1)/2)

        i = len(self.values)-1
        while i>0:
            if self.values[i] > self.values[parent(i)]:
                self.values[i], self.values[parent(i)] = self.values[parent(i)], self.values[i]
                i = parent(i)
            else:
                break
    
    def extractMax(self):
        if self.values == []:
            return None
        if len(self.values) == 1:
            return self.values.pop()
        maxRoot = self.values[0]
        self.values[0] = self.values.pop()
        self.bubbleDown()
        return maxRoot
        
    def bubbleDown(self):
        def child(i):
            return 2*i+2
        i = 0
        while True:
            LChildIndex = child(i)-1
            RChildIndex = child(i)
            if LChildIndex < len(self.values) and RChildIndex < len(self.values) and self.values[i] < self.values[LChildIndex] and self.values[i] < self.values[RChildIndex]:
                #if both children are bigger, use the bigger child
                if self.values[LChildIndex] > self.values[RChildIndex]:
                    #use LHS
                    self.values[i], self.values[LChildIndex] = self.values[LChildIndex], self.values[i]
                    i = LChildIndex
                else:
                    #use RHS
                    self.values[i], self.values[RChildIndex] = self.values[RChildIndex], self.values[i]
                    i = RChildIndex
            elif LChildIndex < len(self.values) and self.values[i] < self.values[LChildIndex]:
                #use LHS
                self.values[i], self.values[LChildIndex] = self.values[LChildIndex], self.values[i]
                i = LChildIndex
            elif RChildIndex < len(self.values) and self.values[i] < self.values[RChildIndex]:
                #use RHS
                self.values[i], self.values[RChildIndex] = self.values[RChildIndex], self.values[i]
                i = RChildIndex
            else:
                break
        
        
        
heap = MaxBHeap()
print(heap.extractMax())
print(heap)

heap = MaxBHeap()
heap.insert(55)
print(heap)
heap.insert(1)
print(heap)
heap.insert(45)
print(heap)



import math

class MinBHeap():
    def __init__(self):
        self.values = []

    def __str__(self):
        return ", ".join(str(x) for x in self.values)

    def insert(self,value):
        self.values.append(value)
        self.bubbleUp()
        return True

    def bubbleUp(self):
        def parent(i):
            return math.floor((i-1)/2)
        def child(i):
            return 2*i+2

        i = len(self.values)-1
        while i>0:
            if self.values[i] < self.values[parent(i)]:
                self.values[i], self.values[parent(i)] = self.values[parent(i)], self.values[i]
                i = parent(i)
            else:
                break

heap = MaxBHeap()
heap.insert(55)
print(heap)
heap.insert(1)
print(heap)
heap.insert(45)
print(heap)
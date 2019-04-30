import math

class Node():
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue():
    def __init__(self):
        self.values = []

    def __str__(self):
        return ", ".join("({}, {})".format(x.value, x.priority) for x in self.values)

    def enqueue(self, value, priority):
        newNode = Node(value, priority)
        self.values.append(newNode)
        self.bubbleUp()
        return True

    def bubbleUp(self):
        def parent(i):
            return math.floor((i-1)/2)

        i = len(self.values)-1
        while i>0:
            if self.values[i].priority < self.values[parent(i)].priority:
                self.values[i], self.values[parent(i)] = self.values[parent(i)], self.values[i]
                i = parent(i)
            else:
                break
    
    def dequeue(self):
        if self.values == []:
            return None
        if len(self.values) == 1:
            return self.values.pop()
        dequeuedNode = self.values[0]
        self.values[0] = self.values.pop()
        self.bubbleDown()
        return dequeuedNode
        
    def bubbleDown(self):
        def child(i):
            return 2*i+2
        i = 0
        while True:
            LChildIndex = child(i)-1
            RChildIndex = child(i)
            if LChildIndex < len(self.values) and RChildIndex < len(self.values) and self.values[i].priority > self.values[LChildIndex].priority and self.values[i].priority > self.values[RChildIndex].priority:
                #if both children are bigger, use the bigger child
                if self.values[LChildIndex].priority < self.values[RChildIndex].priority:
                    #use LHS
                    self.values[i], self.values[LChildIndex] = self.values[LChildIndex], self.values[i]
                    i = LChildIndex
                else:
                    #use RHS
                    self.values[i], self.values[RChildIndex] = self.values[RChildIndex], self.values[i]
                    i = RChildIndex
            elif LChildIndex < len(self.values) and self.values[i].priority > self.values[LChildIndex].priority:
                #use LHS
                self.values[i], self.values[LChildIndex] = self.values[LChildIndex], self.values[i]
                i = LChildIndex
            elif RChildIndex < len(self.values) and self.values[i].priority > self.values[RChildIndex].priority:
                #use RHS
                self.values[i], self.values[RChildIndex] = self.values[RChildIndex], self.values[i]
                i = RChildIndex
            else:
                break
        
class Node():
    
    def __init__(self, value):
        self.value = value
        self.nxt = None
    
class Queue():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def __len__(self):
        return self.size
        
    def __str__(self):
        current = self.first
        string = str(current.value)
        while current.nxt != None:
            current = current.nxt
            string = "{}, {}".format(string,str(current.value))
        return string
        
    def enqueue(self,value):
        newNode = Node(value)
        if self.first == None:
            self.first = newNode
            self.last = self.first
        else:
            self.last.nxt = newNode
            self.last = newNode
        self.size+=1
        return self.size
        
    def dequeue(self):
        if self.first == None:
            return None
        elif self.first == self.last:
            shiftNode = self.first
            self.first = None
            self.last = None
        else:
            dequeueNode = self.first
            self.first = self.first.nxt
        self.size-=1 
        return self.size
        
    
        
myQueue = Queue()
myQueue.enqueue(0)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
print(myQueue)
print(len(myQueue))
myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
print(len(myQueue))
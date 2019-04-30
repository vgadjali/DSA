class Node():
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.nxt = None
    

class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        current = self.head
        string = str(current.value)
        while current.nxt != None:
            current = current.nxt
            string = "{}, {}".format(string,str(current.value))
        return string
    
    def traverse(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.nxt
        
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nxt = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length+=1
        return self
        
    def pop(self):
        if self.length == 0:
            return None
        popNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = popNode.prev
            self.tail.nxt = None
            popNode.prev = None
        self.length -=1 
        return popNode
        
    def shift(self):
        if self.length == 0:
            return None
        shiftNode = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nxt
            self.head.prev = None
            shiftNode.nxt = None 
        self.length -=1 
        return shiftNode
        
    def unshift(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.nxt = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length +=1 
        return self
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.head
        elif index == self.length-1:
            return self.tail
        elif index <= self.length/2:
            #start from beginning
            current = self.head
            for i in range(index):
                current = current.nxt
        else:
            #start from end
            current = self.tail
            for i in range(self.length-index-1):
                current = current.prev
        return current
    
    def set(self, index, value):
        myNode = self.get(index)
        if myNode:
            myNode.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.unshift(value)
            return True
        elif index == self.length:
            self.push(value)
            return True
        else:
            newNode = Node(value)
            counter = 0
            prevNode = self.get(index-1)
            nxtNode = prevNode.nxt
            prevNode.nxt = newNode
            newNode.prev = prevNode
            newNode.nxt = nxtNode
            nxtNode.prev = newNode
            self.length +=1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.shift()
        elif index == self.length-1:
            self.pop()
        else:
            rmvNode = self.get(index)
            prevNode = rmvNode.prev
            nxtNode = rmvNode.nxt
            prevNode.nxt = nxtNode
            nxtNode.prev = prevNode
            rmvNode.prev = None
            rmvNode.nxt = None
            self.length-=1
            return rmvNode

    def reverse(self):
        if self.length < 2:
            return self
        else:
            current = self.head
            newHead = self.tail
            newTail = self.head
            while current:
                current.prev, current.nxt = current.nxt, current.prev
                current = current.prev
            self.head = newHead
            self.tail = newTail
            return self



class Node():
    
    def __init__(self, value):
        self.value = value
        self.nxt = None
        
#first = Node("hi")
#first.nxt = Node("there")
#first.nxt.nxt = Node("Danta")
#print(first.value)
#print(first.nxt.value)
#print(first.nxt.nxt.value)

class SinglyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def __str__(self):
        return "head = {}, tail = {}, length = {}".format(self.head, self.tail, self.length)
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.nxt
            
    def push(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.nxt = newNode
            self.tail = newNode
        self.length+=1
        return self
            
    def pop(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            popNode = self.head
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.nxt != self.tail:
                current = current.nxt
            popNode = current.nxt
            self.tail = current
            self.tail.nxt = None
        self.length-=1 
        return popNode
    
    def shift(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            shiftNode = self.head
            self.head = None
            self.tail = None
        else:
            shiftNode = self.head
            self.head = self.head.nxt
        self.length-=1 
        return shiftNode
        
    def unshift(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.nxt = self.head
            self.head = newNode
        self.length+=1
        return self
        
    def getNode(self, index):
        if index == 0:
            return self.head
        elif index == self.length-1:
            return self.tail
        elif index > self.length-1 or index < 0:
            return None
        else:
            i = 0
            current = self.head
            while i < index:
                current = current.nxt
                i+=1
            return current
    
    def setNode(self, index, value):
        myNode = self.getNode(index)
        if myNode:
            myNode.value = value
            return True
        else:
            return False
            
    def insert(self, index, value):
        if index == 0:
            self.unshift(value)
            return True
        elif index == self.length-1:
            self.push(value)
            return True
        elif index < 0 or index >= self.length:
            return False
        else:
            newNode = Node(value)
            current = self.getNode(index-1)
            #copy next into temp
            tempNode = current.nxt
            #place new node into next
            current.nxt = newNode
            #new node.nxt = temp
            newNode.nxt = tempNode
            self.length+=1
            return True
        
    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self.length-1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        else:
            prevNode = self.getNode(index-1)
            deleteMe = prevNode.nxt
            prevNode.nxt = deleteMe.nxt
            self.length-=1
            return deleteMe
        
    def reverse(self):
        current = self.head
        self.head = self.tail #flip heads and tails
        self.tail = current #flip heads and tails
        nextNode = current.nxt
        
        prevNode = None
        for i in range(self.length):
            current.nxt = prevNode
            prevNode = current
            current = nextNode
            #if current.nxt != None:
            nextNode = current.nxt
        
        return self
            
            
    
linkedList = SinglyLinkedList()
linkedList.push("hi")
linkedList.push("there")
linkedList.push("how")
linkedList.push("are")
linkedList.push("you")
linkedList.traverse()
print("----")
linkedList.reverse()
linkedList.traverse()
print("---")
print(linkedList.head.value)
print(linkedList.head.nxt.value)
print(linkedList.tail.value)

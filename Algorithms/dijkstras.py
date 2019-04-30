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
        
class WeightedGraph():
    def __init__(self):
        self.adjacencyList = {}
    
    def __str__(self):
        string = ""
        for vertex, vdict in self.adjacencyList.items():
            string+= "{}: ".format(vertex)
            string+= ", ".join("({},{})".format(neighbor, weight) for neighbor, weight in vdict.items())
            string+="\n"
        return string
        
    def addVertex(self, vertex):
        if(vertex not in self.adjacencyList.keys()):
            self.adjacencyList[vertex] = {}
        
    def addEdge(self, v1, v2, weight):
        if v2 not in self.adjacencyList[v1].keys():
            self.adjacencyList[v1][v2] = weight
        if v1 not in self.adjacencyList[v2].keys():
            self.adjacencyList[v2][v1] = weight
        
    def rmvEdge(self, v1, v2):
        self.adjacencyList[v1].remove(v2)
        self.adjacencyList[v2].remove(v1)
        
    def rmvVertex(self, vertex):
        for v in self.adjacencyList[vertex]:
            self.adjacencyList[v].remove(vertex)
        self.adjacencyList.pop(vertex, None)

    def dijkstras(self, start, end):
        distances = {}
        pq = PriorityQueue()
        prev = {}
        for vertex, vdict in self.adjacencyList:
            if vertex == self:
                distances[vertex] = 0
                pq.enqueue(vertex, 0)
                prev[vertex] = Null
            else:
                distances[vertex] = float("inf")
                pq.enqueue(vertex, float("inf"))
                prev[vertex] = Null
        
        while len(pq.values) > 0:
            vertex = pq.dequeue()
            if vertex == end:
                #WE ARE DONE
                break
            else:
                for v, vdict in self.adjacencyList
        
        data = [start]
        
        
myGraph = WeightedGraph()
myGraph.addVertex("A")
myGraph.addVertex("B")
myGraph.addVertex("C")
myGraph.addVertex("D")
myGraph.addVertex("E")
myGraph.addVertex("F")
myGraph.addEdge("A","B", 5)
myGraph.addEdge("A","C", 5)
myGraph.addEdge("B","D", 5)
myGraph.addEdge("C","E", 5)
myGraph.addEdge("D","E", 5)
myGraph.addEdge("D","F", 5)
myGraph.addEdge("E","F", 5)
print(myGraph)
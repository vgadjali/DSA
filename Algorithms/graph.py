class Graph():
    def __init__(self):
        self.adjacencyList = {}
    
    def __str__(self):
        return "\n".join("({}: {})".format(k, v) for k,v in self.adjacencyList.items())
    
    def addVertex(self, vertex):
        if(vertex not in self.adjacencyList.keys()):
            self.adjacencyList[vertex] = []
        
    def addEdge(self, v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)
        
    def rmvEdge(self, v1, v2):
        self.adjacencyList[v1].remove(v2)
        self.adjacencyList[v2].remove(v1)
        
    def rmvVertex(self, vertex):
        for v in self.adjacencyList[vertex]:
            self.adjacencyList[v].remove(vertex)
        self.adjacencyList.pop(vertex, None)
        
    def dpsR(self, vertex):
        def dpsHelper(vertex):
            for neighbor in self.adjacencyList[vertex]:
                if neighbor not in data:
                    data.append(neighbor)
                    dpsHelper(neighbor)
        data = [vertex]
        dpsHelper(vertex)
        return data
        
    def dpsI(self,vertex):
        s = [vertex]
        data = []
        while s != []:
            vertex = s.pop()
            if vertex not in data:
                data.append(vertex)
                s.extend(self.adjacencyList[vertex])
                print(s)
        return data

    def bfs(self,vertex):
        s = [vertex]
        data = []
        while s != []:
            vertex = s.pop(0)
            if vertex not in data:
                data.append(vertex)
                s.extend(self.adjacencyList[vertex])
        return data
        
myGraph = Graph()
myGraph.addVertex("A")
myGraph.addVertex("B")
myGraph.addVertex("C")
myGraph.addVertex("D")
myGraph.addVertex("E")
myGraph.addVertex("F")
myGraph.addEdge("A","B")
myGraph.addEdge("A","C")
myGraph.addEdge("B","D")
myGraph.addEdge("C","E")
myGraph.addEdge("D","E")
myGraph.addEdge("D","F")
myGraph.addEdge("E","F")
print(myGraph)
print(myGraph.dpsR("A"))
print(myGraph.dpsI("A"))
print(myGraph.bfs("A"))
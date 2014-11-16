__author__ = 'Java'
from queue import Queue
from queue import PriorityQueue
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.isExplored = False
        self.startExploreTime = -1
        self.finishExploreTime = -1
        self.dist = 10000000000000000000
        self.prev = None

    def addNeighbor(self, nbr, cost=0):
        self.connectedTo[nbr.id] = cost

    def getOutEdges(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr.id]

    def explore(self):
        self.isExplored = True


class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item



class OrientedGraph:
    def __init__(self):
        self.timer = 0
        self.vertexList = {}
        self.numVertices = 0
        self.haveCycle = False
        self.TopologoSortReverse = []
        self.que = Queue()
        self.prior = MyPriorityQueue()

    def addVertexById(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertexList[id] = newVertex
        return newVertex

    def getVertexById(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertexList.keys():
            nv = self.addVertexById(t)
        self.vertexList[f].addNeighbor(self.vertexList[t],cost)

    def getVerticesIds(self):
        return self.vertexList.keys()

    def DFS(self, vertexId):
        vertex = self.getVertexById(vertexId)
        vertex.explore()
        vertex.startExploreTime = self.timer
        self.timer += 1
        for itm in vertex.getOutEdges():
            if (not self.getVertexById(itm).isExplored):
                self.DFS(itm)

        self.timer+=1
        vertex.finishExploreTime = self.timer
        self.TopologoSortReverse.append(vertex.getId())
    def BFS(self,vertexId):
        vertex = self.getVertexById(vertexId)
        self.que.put(vertex)
        vertex.dist = 0
        vertex.prev = None
        while(not self.que.empty()):
            currentVertex = self.que.get()
            for neighborId in currentVertex.connectedTo:
                neighbor = self.getVertexById(neighborId)
                if(neighbor.dist > 1000000):
                    self.que.put(neighbor)
                    neighbor.dist = currentVertex.dist + 1
                    neighbor.prev = currentVertex
    def Dijkstra(self,vertexId):
        vertex = self.getVertexById(vertexId)
        vertex.dist = 0
        for vert in self.vertexList.values():
            self.prior.put(vert,vert.dist)
        while(not self.prior.empty()):
            currentVertex = self.prior.get()
            for neighborId in currentVertex.connectedTo:
                neighbor = self.getVertexById(neighborId)
                if(neighbor.dist>currentVertex.dist + currentVertex.connectedTo[neighborId]):
                    neighbor.dist = currentVertex.dist + currentVertex.connectedTo[neighborId]
                    neighbor.prev = currentVertex
                    self.prior.put(neighbor,neighbor.dist)


    def ExploreGraph(self):
        for itm in self.getVerticesIds():
            if (not self.getVertexById(itm).isExplored):
                 self.DFS(itm)
vertexEdgesInput = input()
vertexEdgesInputTokens = vertexEdgesInput.split()
vertexCount = int(vertexEdgesInputTokens[0])
edgesCount = int(vertexEdgesInputTokens[1])

myGraph = OrientedGraph()
for vertexId in range(1, vertexCount + 1):
    myGraph.addVertexById(vertexId)

for edges in range(0, edgesCount):
    edgesInput = input()
    edgesInputTokens = edgesInput.split()
    fr = int(edgesInputTokens[0])
    to = int(edgesInputTokens[1])
    cost = int(edgesInputTokens[2])

    if(to in myGraph.getVertexById(fr).connectedTo.keys()):
        if(myGraph.getVertexById(fr).connectedTo[to]>cost):
            myGraph.addEdge(fr, to, cost)
    else:
        myGraph.addEdge(fr, to, cost)
ABinput = input()
ABinputTokens = ABinput.split()
A = int(ABinputTokens[0])
B = int(ABinputTokens[1])
myGraph.Dijkstra(A)


def CalculateCost():
    if (myGraph.getVertexById(B).dist > 100000000):
        return -1
    else:
        commonCost = 0
        currentVertex = myGraph.getVertexById(B)
        while (currentVertex.prev != None):
            commonCost += currentVertex.prev.connectedTo[currentVertex.getId()]
            currentVertex = currentVertex.prev
        return commonCost


print(CalculateCost())


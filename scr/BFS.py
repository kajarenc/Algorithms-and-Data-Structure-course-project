__author__ = 'Java'
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.isExplored = False
        self.startExploreTime = -1
        self.finishExploreTime = -1
        self.dist = 1000000
        self.prev = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr.id] = weight

    def getOutEdges(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr.id]

    def explore(self):
        self.isExplored = True
from queue import Queue

class OrientedGraph:
    def __init__(self):
        self.timer = 0
        self.vertexList = {}
        self.numVertices = 0
        self.haveCycle = False
        self.TopologoSortReverse = []
        self.que = Queue()

    def addVertexById(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertexList[id] = newVertex
        return newVertex

    def getVertexByID(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertexList.keys():
            nv = self.addVertexById(t)
        self.vertexList[f].addNeighbor(self.vertexList[t])

    def getVerticesIDs(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    def DFS(self, vertexId):
        vertex = self.getVertexByID(vertexId)
        vertex.explore()
        vertex.startExploreTime = self.timer
        self.timer += 1
        for itm in vertex.getOutEdges():
            if (not self.getVertexByID(itm).isExplored):
                self.DFS(itm)

        self.timer+=1
        vertex.finishExploreTime = self.timer
        self.TopologoSortReverse.append(vertex.getId())
    def BFS(self,vertexId):
        vertex = self.getVertexByID(vertexId)
        self.que.put(vertex)
        vertex.dist = 0
        vertex.prev = None
        while(not self.que.empty()):
            currentVertex = self.que.get()
            for neighborId in currentVertex.connectedTo:
                neighbor = self.getVertexByID(neighborId)
                if(neighbor.dist == 1000000):
                    self.que.put(neighbor)
                    neighbor.dist = currentVertex.dist + 1
                    neighbor.prev = currentVertex

    def ExploreGraph(self):
        for itm in self.getVerticesIDs():
            if (not self.getVertexByID(itm).isExplored):
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
    myGraph.addEdge(fr, to)
    myGraph.addEdge(to,fr)
ABinput  = input()
ABinputTokens = ABinput.split()
A = int(ABinputTokens[0])
B = int(ABinputTokens[1])
myGraph.BFS(A)

def CalculateDist():
    if(myGraph.getVertexByID(B).dist == 1000000):
        return -1
    else:
        rebra = 0
        prevVertex=  myGraph.getVertexByID(B)
        while(prevVertex!=None):
            rebra+=1
            prevVertex = prevVertex.prev
        return rebra-1

print(CalculateDist())


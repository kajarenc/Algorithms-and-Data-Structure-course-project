class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.isExplored = False
    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr.id] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr.id]
    def explore(self):
        self.isExplored = True

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
    def addVertexById(self,id):
        self.numVertices+=1
        newVertex = Vertex(id)
        self.vertexList[id] = newVertex
        return newVertex
    def getVertexByID(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertexList
    def addEdge(self,f,t,cost = 0):
        if f not in self.vertexList.keys():
            nv = self.addVertexById(t)
        self.vertexList[f].addNeighbor(self.vertexList[t],cost)
        self.vertexList[t].addNeighbor(self.vertexList[f],cost) # for non oriented graph
    def getVertices(self):
        return self.vertexList.keys()
    def __iter__(self):
        return iter(self.vertexList.values())




vertexEdgesInput = input()
vertexEdgesInputTokens = vertexEdgesInput.split()
vertexCount  = int(vertexEdgesInputTokens[0])
edgesCount  = int(vertexEdgesInputTokens[1])

myGraph = Graph()
vertices = {}
for vertexId in range(1,vertexCount+1):
    myGraph.addVertexById(vertexId)

for edges in range(0,edgesCount):
    edgesInput  = input()
    edgesInputTokens = edgesInput.split()
    fr = int(edgesInputTokens[0])
    to = int(edgesInputTokens[1])
    myGraph.addEdge(fr,to)

uvInput = input()
uvInputTokens = uvInput.split()
u = int(uvInputTokens[0])
v = int(uvInputTokens[1])

def exploreNeighbors(vertexId):
    vertex = myGraph.getVertexByID(vertexId)
    vertex.explore()
    for itm in vertex.getConnections():
        if(not myGraph.getVertexByID(itm).isExplored):
            exploreNeighbors(itm)
exploreNeighbors(u)
print(int(myGraph.getVertexByID(v).isExplored))






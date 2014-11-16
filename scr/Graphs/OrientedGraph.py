__author__ = 'Java'
from Graphs.Vertex import Vertex
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






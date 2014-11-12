__author__ = 'Java'
from Graphs.Vertex import Vertex
class NonOrientedGraph:
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
        self.vertexList[t].addNeighbor(self.vertexList[f],cost) #
    def getVerticesIDs(self):
        return self.vertexList.keys()
    def __iter__(self):
        return iter(self.vertexList.values())
    def exploreNeighbors(self, vertexId):
        vertex = self.getVertexByID(vertexId)
        vertex.explore()
        for itm in vertex.getConnections():
            if (not self.getVertexByID(itm).isExplored):
                self.exploreNeighbors(itm)

    def exploreGraph(self):
        connectedComponentNumber = 0
        for itm in self.getVertices():
            if (not self.getVertexByID(itm).isExplored):
                connectedComponentNumber += 1
                self.exploreNeighbors(itm)
        return connectedComponentNumber




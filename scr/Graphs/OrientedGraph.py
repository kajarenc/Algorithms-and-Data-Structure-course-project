__author__ = 'Java'
from Graphs.Vertex import Vertex


class OrientedGraph:
    def __init__(self):
        self.timer = 0
        self.vertexList = {}
        self.numVertices = 0
        self.haveCycle = False
        self.TopologoSortReverse = []

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

    def __contains__(self, item):
        return item in self.vertexList

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


    def ExploreGraph(self):
        for itm in self.getVerticesIDs():
            if (not self.getVertexByID(itm).isExplored):
                 self.DFS(itm)






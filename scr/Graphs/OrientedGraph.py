__author__ = 'Java'
from Graphs.Vertex import Vertex
from queue import Queue
from queue import PriorityQueue

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






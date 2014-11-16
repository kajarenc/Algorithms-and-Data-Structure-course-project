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
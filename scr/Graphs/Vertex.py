class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.isExplored = False
        self.startExploreTime = -1
        self.finishExploreTime = -1

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
from Graphs.OrientedGraph import OrientedGraph
vertexEdgesInput = input()
vertexEdgesInputTokens = vertexEdgesInput.split()
vertexCount = int(vertexEdgesInputTokens[0])
edgesCount = int(vertexEdgesInputTokens[1])

myGraph = OrientedGraph()
vertices = {}
for vertexId in range(1, vertexCount + 1):
    myGraph.addVertexById(vertexId)

for edges in range(0, edgesCount):
    edgesInput = input()
    edgesInputTokens = edgesInput.split()
    fr = int(edgesInputTokens[0])
    to = int(edgesInputTokens[1])
    myGraph.addEdge(fr, to)
myGraph.ExploreGraph()
print(int(myGraph.haveCycle))


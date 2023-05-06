# Contents: Graph Construction/Ops, BFS/DFS, Q

for name in dir():
    if not name.startswith('_'):
        del globals()[name]

# Difference than Trees: Can be cyclic --> use boolean to avoid double counting

# -----------------------------------
# Representations: edge = u, vertex = v

# 1) Adjacency Matrix: Vertex v is connected to vertex w by an edge whose value A[v][w]
# - most matrices are sparse --> most edges are missing --> wasted space --> don't use this one
# implement!

# 2) Lists of Edges:
# implement!

# 3) Adjacency List: A dict keeps v as keys, and it's neighbors (u or w) as values
from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)  # adjecency list

    def addEdge(self, u, v):  # function to add an edge to graph
        self.adj[u].append(v)

    def printGraph(self):
        for u in range(len(self.adj)):
            print(u, "-->", self.adj[u])

# Driver code: 2-->0-->1, 2-->3
g = Graph1()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(3, 4)
g.addEdge(4, 3)
g.printGraph()

# ---
def dfs(g, start, visited):  # DFS iterative
    # stack = []
    isnew = len(g.adj) * [False]  # boolean array
    stack = [start]  # just a starting point
    while len(stack):  # when visited is too full, stack will just keep popping
        v = stack.pop()  # get vertex
        print(v, stack, visited)

        if not isnew[v]:
            print("new", end=' ')
            isnew[v] = True
            visited.append(v)

        for node in g.adj[v]:  # get all adjacent vertices of v
            if not isnew[node]:  # put each node nearby in the stack
                stack.append(node)
    return visited

dfs(g, 2, [])  # 2- 0-1 - 3-4 or  2- 3-4 - 0-1
dfs(g, 3, [])  # 3-4 because no path from 3 back to 2


def bfs(g, start, visited=[]):  # BFS iterative
    isnew = len(g.adj) * [False]
    stack = [node]
    while q:
        v = q.pop(0)
        if not v in visited:
            visited = visited + [v]
            q = q + graph[v]
            return visited
            # 2 - 1-4 - 3-0
bfs(g, 2, [])  # 2 - 3-0 - 1-4


# --alternative
class Vertex:  #
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}   # adjacency list

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


# Create Vertex for each key -->
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):      # add vertices
    g.addVertex(i)
g.vertList
g.getVertices()         # similar
4 in g                  # check if a vertex exists
print(g.getVertex(4))

g.addEdge(0, 1, 1)  # add Edges to connect Vertices
g.addEdge(0, 5, 1)  # addEdge(fromVert, toVert, weight), weight optional
g.addEdge(1, 2, 1)
g.addEdge(2, 3, 1)
g.addEdge(3, 4, 1)
g.addEdge(3, 5, 1)
for v in g:  # verify each Edge w/ a nested loop
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))


# -----------------------------------
# BFS: O(V+E), 1 --> 2+3 --> 4+5 --> 6
# http://interactivepython.org/courselib/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html

def iterative_bfs(graph, start, path=[]):
    '''iterative breadth first search from start'''
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path + [v]
            q = q + graph[v]
    return path

# def recursive_bfs


# -----------------------------------
# DFS: O(V+E)/  A --> B --> D/E --> F --> popF --> C --> popE --> popD --> popB --> popA
# - Maark the current v as being visited, explore each adjacent v that is not visited before
# - Use Stack to keep the visited memory
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

def iterative_dfs(graph, start, path=[]):
    '''iterative depth first search from start'''
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path

def recursive_dfs(graph, start, path=[]):
    '''recursive depth first search from start'''
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
print('recursive dfs ', recursive_dfs(graph, 'A'))
print('iterative dfs ', iterative_dfs(graph, 'A'))
print('iterative bfs ', iterative_bfs(graph, 'A'))

# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

start = 'A'
q = [start]
while q:
    v = q.pop(0)
    if not v in path:
        path = path + [v]
        q = q + graph[v]
print(q)


# -----------------------------------
# Graph 01: Find Itinerary from a given list of tickets
# Given:
d = {"D": "E", "A": "B", "C": "D", "B": "C"}  # A-->B-->C-->D-->E

# Sol 1: Hashmap to build a graph, and traverse it from end to start


# Dijkstra
# 5) A*
# 6) N choose K
# 7) The Word Ladder Problem   (FOOL --> SAGE, use BFS)

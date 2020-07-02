from queue import Queue


class Graph:
    def __init__(self, V):
        self.vertices = [Vertex() for i in range(V)]

    def addEdges(self, V, E):
        self.vertices[V].edges.extend(E)


class Vertex:
    def __init__(self):
        self.visited = False
        self.entry = 0
        self.process = 0
        self.edges = []
        self.parent = None
        self.d = 0


def BFS(G: Graph, s):
    Q = Queue()
    for v in G.vertices:
        v.visited = False
    s.d = 0
    s.visited = True
    s.parent = None
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.edges:
            if not G.vertices[v].visited:
                G.vertices[v].visited = True
                G.vertices[v].d = u.d + 1
                G.vertices[v].parent = u
                Q.put(G.vertices[v])


def DFS(G):
    def DFSVisit(u):
        nonlocal time
        time += 1
        u.visited = True
        u.entry = time
        for i in u.edges:
            if not G.vertices[i].visited:
                G.vertices[i].parent = u
                DFSVisit(G.vertices[i])
        time += 1
        u.process = time

    time = 0
    for v in G.vertices:
        v.visited = False
        v.parent = None
    for v in G.vertices:
        if not v.visited:
            DFSVisit(v)


# a = Graph(6)
# a.addEdges(0, [1, 2])
# a.addEdges(1, [2])
# a.addEdges(2, [4])
# a.addEdges(4, [3, 5])
# a.addEdges(5, [0])
#
# BFS(a, a.vertices[0])
# for i in range(0, len(a.vertices)):
#     print(i+1, a.vertices[i].d)

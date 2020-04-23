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


class Kueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def get(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


def tasks(A: list):
    A.sort(key=lambda tup: tup[0])
    Cbusy = (False, 0)
    Jbusy = (False, 0)
    res = ""
    for i in A:
        if not Cbusy[0] or Cbusy[1] <= i[0]:
            res += "C"
            Cbusy = (True, i[1])
        elif not Jbusy or Jbusy[1] <= i[0]:
            res += "J"
            Jbusy = (True, i[1])
        else:
            return "IMPOSSIBLE"
    return res


def width(S, word: str):
    F = [0]*len(word)
    for i in range(len(F)):
        for s in S:
            substr = word[max(0, i-len(s)+1):i+1]
            print(s, substr)
            if s == substr:
                if i - len(s) >= 0:
                    F[i] = max(F[i], min(len(s), F[i-len(s)]))
                else:
                    F[i] = max(F[i], len(s))
    print(F)
    return F[-1]


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
#
# b = Kueue()
# for i in range(5):
#     b.push(i)
# for i in range(5):
#     print(b.get())

# print(tasks([(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]))
print(width(["ab", "abab", "ba", "bab", "b"], "ababbab"))

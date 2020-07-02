from queue import PriorityQueue


def relax(u, v, w, d, parents):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parents[v] = u
        return True
    return False


# Konstruuje najtańsze ścieżki jeden-każdy, wagi to liczby >=0, O(E*logV)
def dijkstra(A, s, t):
    Q = PriorityQueue()
    d = [float("inf")]*len(A)
    d[s] = 0
    parents = [None]*len(A)
    Q.put((0, s))
    while not Q.empty():
        _, u = Q.get()
        for v, w in A[u]:
            if relax(u, v, w, d, parents):
                Q.put((d[v], v))
    while t is not None:
        print(t, end=" ")
        t = parents[t]


def relax2(A, u, v, d, parents):
    if d[v] > d[u] + A[v]:
        d[v] = d[u] + A[v]
        parents[v] = u
        return True
    return False


def dijkstra2(A, s):
    Q = PriorityQueue()
    d = [float("inf")]*len(A)
    d[s] = 0
    parents = [None]*len(A)
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(len(A[u])):
            if A[u][i] != 0 and relax2(A, u, i, d, parents):
                Q.put(i)
    return parents


# Konstruuje najtańsze ścieżki jeden-każdy, wagi mogą być ujemne, potrafi stwierdzić cykl ujemny, O(V*E)
def bellman_ford(A, s, t):
    d = [float("inf")] * len(A)
    d[s] = 0
    parents = [None] * len(A)
    for i in range(len(A)-1):
        for j in range(len(A)):
            for k in A[j]:
                relax(j, k, d, parents)
    for j in range(len(A)):
        for k in A[j]:
            if d[k[0]] > d[j] + k[1]:
                print("Cykl ujemny")
                return
    while t is not None:
        print(t, end=" ")
        t = parents[t]


# Konstruuje najtańsze ścieżki każdy-każdy, O(V^3)
def floyd_warshall(W):
    n = len(W)
    S = W[:]
    P = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if W[i][j] < float("inf"):
                P[i][j] = i
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][j] > S[i][t] + S[t][j]:
                    P[i][j] = P[t][j]
                    S[i][j] = S[i][t] + S[t][j]
    return S, P


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def make_set(x):
    return Node(x)


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# Znajduje minimalne drzewo rozpinające w grafie spójnym, nieskierowanym - najtańszy zbiór krawędzi pokrywających
# wszystkie wierzchołki, O(ElogV)
def Kruskal(G):
    edges = []
    result = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G[i])):
            edges.append((i, G[i][j][0], G[i][j][1]))
    edges.sort(key=lambda tup: tup[2])

    vertices = []
    for i in range(len(G)):
        vertices.append(make_set(i))

    for (u, v, w) in edges:
        if find_set(vertices[u]) != find_set(vertices[v]):
            result[u].append((v, w))
            result[v].append((u, w))
            union(vertices[u], vertices[v])
    return result


def relaxPrim(u, v, w, d, parents):
    if parents[u] != v and d[v] > w:
        d[v] = w
        parents[v] = u
        return True
    return False


# Znajduje minimalne drzewo rozpinające - najtańszy zbiór krawędzi pokrywających wszystkie wierzchołki, O(ElogV)
def Prim(A, s):
    Q = PriorityQueue()
    d = [float("inf")]*len(A)
    d[s] = 0
    parents = [None]*len(A)
    Q.put((0, s))
    while not Q.empty():
        _, u = Q.get()
        for v, w in A[u]:
            if relaxPrim(u, v, w, d, parents):
                Q.put((w, v))
    return parents


a = [[(1, 3), (2, 2)], [(0, 3), (3, 2), (4, 1)], [(0, 2), (5, 1), (6, 3)],
     [(1, 2), (7, 5)], [(1, 1), (5, 7), (7, 1)], [(2, 1), (6, 1), (8, 2)],
     [(2, 3), (5, 1), (8, 8)], [(3, 5), (4, 1), (8, 20)], [(5, 2), (6, 8), (7, 20)]]

b = [[(1, 3), (2, 2)], [(0, 3), (3, 2), (4, 1)], [(0, 2), (5, 1), (6, 3)],
     [(1, 2), (7, -5)], [(1, 1), (5, 7), (7, 1)], [(2, 1), (6, 1), (8, 2)],
     [(2, 3), (5, 1), (8, 8)], [(3, 5), (4, 1), (8, 20)], [(5, 2), (6, 8), (7, 20)]]

c = [
[float("inf"), 3, 2, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
[3, float("inf"), float("inf"), 2, 1, float("inf"), float("inf"), float("inf"), float("inf")],
[2, float("inf"), float("inf"), float("inf"), float("inf"), 1, 3, float("inf"), float("inf")],
[float("inf"), 2, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 5, float("inf")],
[float("inf"), 1, float("inf"), float("inf"), float("inf"), 7, float("inf"), 1, float("inf")],
[float("inf"), float("inf"), 1, float("inf"), 7, float("inf"), 1, float("inf"), 2],
[float("inf"), float("inf"), 3, float("inf"), float("inf"), 1, float("inf"), float("inf"), 8],
[float("inf"), float("inf"), float("inf"), 5, 1, float("inf"), float("inf"), float("inf"), 20],
[float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2, 8, 20, float("inf")],
]

r = [
[(1, 2), (2, 6), (4, 1)],
[(0, 2), (3, 3)],
[(0, 6), (5, 8)],
[(1, 3), (4, 2), (6, 1)],
[(0, 1), (3, 2), (5, 5)],
[(2, 8), (4, 5), (6, 7)],
[(5, 7), (3, 1)],
]

dijkstra(a, 0, 8)
print("")
# bellman_ford(a, 0, 8)
# print("")
# i, j = floyd_warshall(c)
# for s in i:
#     print(s)
# print("")
# for s in j:
#     print(s)
# for i in Kruskal(r):
#     print(i)
print(Prim(r, 0))

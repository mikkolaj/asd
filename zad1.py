# Rozwiązaniem jest zaimplementowany algorytm Forda Fulkersona
from queue import Queue


def max_flow(G, s, t):
    parents = [None]*len(G)
    maks_flow = 0
    graph = G[:]
    # dopóki istnieje ścieżka powiększająca, szukaj większego przepływu
    while BFS(G, s, t, parents):
        path_flow = float("inf")
        end = t
        # szukamy minimalnej przepustowości
        while end != s:
            path_flow = min(path_flow, graph[parents[end]][end])
            end = parents[end]
        maks_flow += path_flow
        end = t
        # odejmujemy i dodajemy wartość minimalnego przepływu do odpowiednich krawędzi w sieci residualnej
        while end != s:
            u = parents[end]
            graph[u][end] -= path_flow
            graph[end][u] += path_flow
            end = parents[end]
    return maks_flow


def BFS(G, s, t, parents):
    Q = Queue()
    visited = [False]*len(G)
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in range(len(G[s])):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.put(v)
    return True if visited[t] else False


c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( max_flow( c, 0, 3 ) )  # wypisze 3
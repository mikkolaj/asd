from queue import PriorityQueue


def relax(u, v, d, parents):
    if d[v[0]] > d[u] + v[1]:
        d[v[0]] = d[u] + v[1]
        parents[v[0]] = u
        return True
    return False


def dijkstra(A, s):
    Q = PriorityQueue()
    d = [float("inf")]*len(A)
    d[s] = 0
    parents = [None]*len(A)
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in A[u]:
            if relax(u, i, d, parents):
                Q.put(i[0])
    return parents


G = [[(1,0), (2,1)],[(3,1), (2,0)],[(3,0)],[]]
print( dijkstra( G, 0 ) )  # wypisze [None,0,1,2]
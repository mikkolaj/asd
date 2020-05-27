# Sortowanie topologiczne - wywołaj DFS i po przetworzeniu wierzchołka dopisz go na początek tworzonej listy


def Sort(G):
    def DFSVisit(G, u, visited, sorteed):
        visited[u] = True
        for i in G[u]:
            if not visited[i]:
                DFSVisit(G, i, visited, sorteed)
        sorteed.append(u)

    visited = [False]*len(G)
    sorteed = []
    for v in range(len(G)):
        if not visited[v]:
            DFSVisit(G, v, visited, sorteed)
    return list(reversed(sorteed))


# Znajdowanie cyklu Eulera - wywołujemy DFS bez uwzględniania pól visited, zamiast tego usuwamy krawędzie, po których
# już przeszliśmy, w momencie przetworzenia wierzchołka dodajemy go na początek tworzonego cyklu


def EulerCycle(G):
    def DFSVisit(G, u, stack):
        for i in G[u]:
            G[u].remove(i)
            G[i].remove(u)
            stack.append(i)
            DFSVisit(G, i, stack)
        if len(G[u]) == 0:
            cycle.append(stack.pop())

    stack = []
    cycle = []
    for v in range(len(G)):
        if len(G[v]) > 0:
            stack.append(v)
            DFSVisit(G, v, stack)
    return cycle


# Silnie spójne składowe

def DFS(G):
    def DFSVisit(G, u, visited, time):
        visited[u] = True
        for i in G[u]:
            if not visited[i]:
                time = DFSVisit(G, i, visited, time)
        time += 1
        times.append([u, time])
        return time

    visited = [False]*len(G)
    time = 0
    times = []
    for v in range(len(G)):
        if not visited[v]:
            time = DFSVisit(G, v, visited, time)
    return times


def DFS2(G, times):
    def DFSVisit2(G, u, visited, silnie, licz):
        visited[u] = True
        silnie[licz].append(u)
        for i in G[u]:
            if not visited[i]:
                DFSVisit2(G, i, visited, silnie, licz)

    visited = [False]*len(G)
    silnie = []
    licz = -1
    for (v, time) in times:
        if not visited[v]:
            silnie.append([])
            licz += 1
            DFSVisit2(G, v, visited, silnie, licz)
    return silnie


def reverseGraph(G):
    new = [[] for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            new[v].append(u)
    return new


def SilnieSpojne(G):
    times = DFS(G)
    times.reverse()
    R = reverseGraph(G)
    return DFS2(R, times)


# Mosty

def DFSMost(G):
    def DFSVisit(G, u, visited, parents, backward, time):
        visited[u] = True
        time += 1
        times[u] = time
        for i in G[u]:
            if visited[i] and i != parents[u] and len(backward[i]) == 0:
                backward[u].append(i)
            if not visited[i]:
                parents[i] = u
                time = DFSVisit(G, i, visited, parents, backward, time)
        return time

    parents = [None]*len(G)
    visited = [False]*len(G)
    backward = [[] for _ in range(len(G))]
    time = 0
    times = [None]*len(G)
    for v in range(len(G)):
        if not visited[v]:
            time = DFSVisit(G, v, visited, parents, backward, time)
    return backward, times, parents


def Mosty(G):
    backward, times, parents = DFSMost(G)
    low = [None]*len(G)
    for v in range(len(G)):
        low[v] = times[v]
        for i in backward[v]:
            low[v] = min(low[v], times[i])
            p = parents[v]
            while p != i:
                low[p] = min(low[p], low[v])
                p = parents[p]
    mosty = []
    for v in range(1, len(G)):
        if low[v] == times[v]:
            mosty.append((v, parents[v]))
    return mosty


def PunktyArtykulacji(G):
    backward, times, parents = DFSMost(G)
    print(times, parents, backward)
    low = [None] * len(G)
    for v in range(len(G)):
        low[v] = times[v]
        for i in backward[v]:
            low[v] = min(low[v], times[i])
            p = parents[v]
            while p != i:
                low[p] = min(low[p], low[v])
                p = parents[p]
    points = []
    licz = 0
    for v in G[0]:
        if parents[v] == 0:
            licz += 1
    if licz > 1:
        points.append(0)
    for v in range(1, len(G)):
        if low[v] >= times[parents[v]] and parents[v] != 0:
            points.append(parents[v])
    return points


def knapsack2d(V, max_w, max_h ):
    n = len(V)
    # tworzę sześcian rozmiaru n*(max_w+1)*(max_h+1) na maksymalne profity dla każdego przedmiotu
    F = [[[0]*(max_h+1) for __ in range(max_w+1)] for _ in range(n)]
    # ustawiam początkowe wartości dla zerowego przedmiotu (musi się zmieścić z wagą i wysokością)
    for i in range(P[0][1], max_w+1):
        for j in range(P[0][2], max_h+1):
            F[0][i][j] = P[0][0]
    return KnapsackRec(V, F, n-1, max_w, max_h)  # w F[n-1][max_w][max_h] będzie maksymalny profit


def KnapsackRec(V, F, i, j, k):
    if F[i][j][k] > 0:  # jeżeli dane pole jest wypełnione, to znamy dla niego profit
        return F[i][j][k]
    if i > 0:  # dla przedmiotów o ineksie większym niż zero musimy policzyć ich wartość
        F[i][j][k] = KnapsackRec(V, F, i-1, j, k)
        # jeżeli przedmiot się mieści, to bierzemy maksimum z profitu z wzięcia przedmiotu i nie wzięcia go
        if j >= V[i][1] and k >= V[i][2]:
            F[i][j][k] = max(F[i][j][k], KnapsackRec(V, F, i-1, j-V[i][1], k-V[i][2]) + V[i][0])
    return F[i][j][k]


P = [(5,10,3), (7,8,12), (2,7,3)]
# print( knapsack2d( P, 16, 15 ))   # wypisze 9

G = [
[1, 5],
[5, 6, 0, 2],
[1, 6, 3, 4],
[2, 4],
[3, 2, 6, 5],
[0, 1, 4, 6],
[1, 2, 4, 5],
]

F = [
[1, 2, 4],
[2, 3],
[],
[5, 6],
[3],
[],
[]
]

H = [
[2, 4],
[0, 9],
[1],
[4, 6],
[5],
[3],
[5],
[3, 9],
[7],
[10],
[8, 6],
]

I = [
[1, 3],
[0, 2],
[1, 3, 4],
[0, 2],
[2, 5, 6],
[4, 6],
[5, 4]
]

J = [
[1, 4],
[0,2,4,3],
[1,3],
[1,2],
[1,0],
]

K = [
[1, 3],
[0, 2],
[1, 3, 4],
[0, 2],
[2, 5, 6],
[4, 6],
[5, 4, 7],
[6, 8],
[7]
]

# print(EulerCycle(G))
# print(Sort(F))
# print(SilnieSpojne(H))
# print(Mosty(I))
print(PunktyArtykulacji(K))


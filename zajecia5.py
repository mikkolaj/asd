def fibboRAK(n):
    if n <= 2:
        return 1
    return fibboRAK(n-1)+fibboRAK(n-2)


def fibboBTR(n):
    F = [None]*(n+1)
    F[1] = F[2] = 1
    for i in range(3, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


def fibboMEM(n):
    F = [0]*(n+1)
    F[1] = F[2] = 1
    return fibboMEMins(F, n)


def fibboMEMins(F, n):
    if F[n] > 0:
        return F[n]
    F[n] = fibboMEMins(F, n-1) + fibboMEMins(F, n-2)
    return F[n]


def fibboBST(n):
    fprev = 1
    fnext = 1
    for i in range(3, n+1):
        fnext, fprev = fnext + fprev, fnext
    return fnext


# F[i] - dlugość najdłuższego podciągu kończącego się na tab[i]
def LIS(tab):
    n = len(tab)
    F = [1]*n
    P = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if tab[i] > tab[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    maks = ind = -1
    for i in range(n):
        if F[i] > maks:
            maks = F[i]
            ind = i
    return maks, P, ind


def printLIS(tab, P, i):
    if P[i] != -1:
        printLIS(tab, P, P[i])
    print(tab[i])


# F[i][j] - największy zysku uzyskany poprzez wzięcie maksymalnie i+1 pierwszych elementów mając j miejsca w plecaku
def Knapsack(P, W, maxW):
    n = len(P)
    F = [[0]*(maxW+1) for i in range(n)]
    for i in range(W[0], maxW+1):
        F[0][i] = P[0]
    for i in range(1, n):
        for w in range(1, maxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])
    wyn = []
    i, w = n-1, maxW
    while i >= 0:
        if w >= W[i] and (i == 0 or F[i-1][w-W[i]] + P[i] > F[i-1][w]):
            wyn.append(i)
            i, w = i-1, w-W[i]
        else:
            i = i-1
    return F[n-1][maxW], wyn


def KnapsackPrep(P, W, maxW):
    n = len(P)
    F = [[0]*(maxW+1) for i in range(n)]
    for i in range(W[0], maxW+1):
        F[0][i] = P[0]
    return KnapsackRec(P, W, n-1, maxW, F)


def KnapsackRec(P, W, i, w, F):
    if F[i][w] > 0:
        return F[i][w]
    if i > 0:
        F[i][w] = KnapsackRec(P, W, i-1, w, F)
        if w >= W[i]:
            F[i][w] = max(F[i][w], KnapsackRec(P, W, i-1, w-W[i], F) + P[i])
    return F[i][w]


class Employee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.name = None
        self.f = -1
        self.g = -1
        self.ftookflist = None
        self.flist = []
        self.glist = []


def f(v: Employee):
    if v.f >= 0:
        return v.f
    x = v.fun
    for i in v.emp:
        x += g(i)
    y = g(v)
    v.f = max(x, y)
    return v.f


def g(v: Employee):
    if v.g >= 0:
        return v.g
    v.g = 0
    for i in v.emp:
        v.g += f(i)
    return v.g


def f1(v: Employee):
    if v.f >= 0:
        if v.ftookflist:
            return v.f, v.flist
        else:
            return v.f, v.glist
    x = v.fun
    v.flist = [v.name]
    for i in v.emp:
        temp = g1(i)
        x += temp[0]
        v.flist.extend(temp[1])
    y, v.glist = g1(v)
    if x > y:
        v.f = x
        v.ftookflist = True
        return v.f, v.flist
    else:
        v.f = y
        v.ftookflist = False
        return v.f, v.glist


def g1(v: Employee):
    if v.g >= 0:
        return v.g, v.glist
    v.g = 0
    for i in v.emp:
        temp = f1(i)
        v.g += temp[0]
        v.glist.extend(temp[1])
    return v.g, v.glist


# czy w tab da się znaleźć sumę s na indeksach od 1 do i
# F[i][j] - czy da się znaleźć sumę j w pierszych i elementach
def suma(tab, i, s):
    F = [[False]*(s+1) for i in range(i+1)]
    for j in range(i+1):
        F[j][0] = True
    for j in range(1, i+1):
        for k in range(1, s+1):
            if k - tab[j-1] >= 0:
                F[j][k] = F[j-1][k] or F[j-1][k-tab[j-1]]
            else:
                F[j][k] = F[j-1][k]
    return F[i][s]


# Najdłuższy wspólny podciąg
# F[i][j] - najdłuższy wspólny podciąg do j-tej pozycji w pierwszym słowie i do i-tej pozycji w drugim słowie
def NWP(A, B):
    n = len(A)
    m = len(B)
    F = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[j-1] == B[i-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[m][n]


# Najdłuższy rosnący podciąg
def NRP(A):
    B = sorted(A)
    return NWP(A, B)


# Najmniejszy koszt wymnożenia wszystkich macierzy w ciągu
# chain - ciąg pierwszych wymiarów kolejnych macierzy (wiersze), musi być podany jeden dodatkowy pod koniec
# F[i][j] - optymalny koszt wymnożenia od i-tej do j-tej macierzy
def MM(chain, n):
    F = [[float("inf")]*n for i in range(n)]
    for i in range(n):
        F[i][i] = 0
    # długość podciągu macierzy
    for length in range(2, n+1):
        # dla każdego przedziału długości length
        for i in range(n-length+1):
            j = i+length-1
            for k in range(i, j):
                # minimum z pomnożenia lewej i prawej części podciągu
                F[i][j] = min(F[i][j], F[i][k] + F[k+1][j] + chain[i] * chain[k+1] * chain[j+1])
    return F[0][n-1]


# Minimalny koszt przejścia z pola (1, 1) w szachownicy na pole (n, n) korzystając tylko z ruchów w dół i w prawo
# F[i][j] - minimalny koszt dotarcia na pole (i, j)
def szachownica(A):
    n = len(A)
    F = [[0]*n for i in range(n)]
    F[0][0] = A[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + A[0][i]
        F[i][0] = F[i-1][0] + A[i][0]
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i][j-1], F[i-1][j]) + A[i][j]
    return F[n-1][n-1]


# Minimalna ilość monet ze zbioru M potrzebna do wydania kwoty w
# F[i] - minimalna ilość monet potrzebna do wydania kwoty i
def wydawanko(M, w):
    F = [0]*(w+1)
    for i in range(1, w+1):
        F[i] = float("inf")
        for j in M:
            if i - j >= 0:
                F[i] = min(F[i], F[i-j]+1)
    return F[w]


W = [4, 2, 1, 1, 12]
P = [10, 2, 1, 2, 4]
S = [3, 1, 2, 4]
R = [3, 1, 7, 6, 7, 4]
print(Knapsack(P, W, 15)[1])
# print(MM(R, len(R)-1))

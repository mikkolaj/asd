def kings_path(A):
    F = [[0]*len(A[0]) for i in range(len(A))]
    print(F)


# A = [[1,1,2],[5,1,3],[4,1,1]]
# print( kings_path( A ) )


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
print( knapsack2d( P, 16, 15 ))   # wypisze 9


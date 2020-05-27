# Algorytm bazujący na algorytmie Floyda-Warshalla, jeżeli istnieje połączenie pośrednie dla S[i][j] poprzez t,
# uzupełniamy S[i][j] jako True


def tclosure(W):
    n = len(W)
    S = W[:]
    for t in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if S[i][j] is False and S[i][t] is True and S[t][j] is True:
                    S[i][j] = True
    return S


G = [ [False, True , False],[False, False, True ],[False, False, False] ]
print( tclosure( G ) )




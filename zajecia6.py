class Lekcja:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def zajecia(lista: Lekcja):
    wyn = [lista[0]]
    m = 1
    while m < len(lista):
        while lista[m].start < wyn[len(wyn)-1].end:
            m += 1
        wyn.append(lista[m])
        m += 1
    return wyn


def heapifyMin(tab, root):
    largest = root
    left = 2*root+1
    right = 2*root+2

    if left < len(tab) and tab[left] < tab[largest]:
        largest = left

    if right < len(tab) and tab[right] < tab[largest]:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapifyMin(tab, largest)


def buildheap(tab):
    for i in range(len(tab)//2, -1, -1):
        heapifyMin(tab, i)


def huffman_len(A):
    buildheap(A)
    res = 0
    while len(A) > 1:  # dopóki w kopcu jest więcej niż jeden element, do sumy dodajemy 2 najmniejsze elementy
        mini, A[0] = A[0], A[len(A)-1]  # zabieramy minimalny element z kopca
        A.pop()
        heapifyMin(A, 0)  # znajdujemy drugi minimalny element
        A[0] += mini  # teraz w A[0] będzie suma dwóch minimalnych
        res += A[0]
        heapifyMin(A, 0)
    return res


def continuousKnapsack(W, P, K):
    A = [(W[i], P[i]/W[i]) for i in range(len(W))]
    A = sorted(A, key=lambda tup: tup[1], reverse=True)
    sum = 0
    for i in A:
        if K > i[0]:
            sum += i[0]*i[1]
            K -= i[0]
        else:
            return sum + K*i[1]
    return sum


def minrefuels(A, maxfuel, end):
    pos = 0  # index
    cur = A[0]
    trasa = []
    while True:
        trasa.append(cur)
        if pos + 1 >= len(A):
            if end - cur[0] <= maxfuel:
                return trasa
            else:
                return None

        pos = pos + 1
        best = A[pos]
        if best[0] - cur[0] > maxfuel:  # nie da się dojechać
            return None

        i = pos + 2
        while i < len(A) and A[i][0] <= maxfuel + cur[0]:
            if A[i][1] < best[1]:
                best = A[i]
                pos = i
            i += 1

        if cur[1] < best[1] and end - cur[0] <= maxfuel:
            return trasa
        cur = best


# P = [7, 2, 5, 10, 8]
# W = [3, 1, 6, 3, 6]
# print(continuousKnapsack(W, P, 7))
test = [(0, 2), (4, 5), (8, 7), (10, 1)]
print(minrefuels(test, 10, 21))



import random
import sys


def quicksort(tab, left, right):
    mid = tab[(left+right)//2]
    i = left
    j = right
    while i <= j:
        while tab[i] < mid:
            i += 1
        while tab[j] > mid:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
    if j > left:
        quicksort(tab, left, j)
    if i < right:
        quicksort(tab, i, right)


def mergesort(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        L = tab[:mid]
        R = tab[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1


def heapify(tab, root):
    largest = root
    left = 2*root
    right = 2*root+1

    if left <= tab[0] and tab[left] > tab[largest]:
        largest = left

    if right <= tab[0] and tab[right] > tab[largest]:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapify(tab, largest)


def heapifyMin(tab, root):
    largest = root
    left = 2*root
    right = 2*root+1

    if left <= tab[0] and tab[left] < tab[largest]:
        largest = left

    if right <= tab[0] and tab[right] < tab[largest]:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapify(tab, largest)


def buildheap(tab):
    for i in range(tab[0]//2, 0, -1):
        heapify(tab, i)


def heapsort(tab):
    buildheap(tab)
    for i in range(tab[0], 1, -1):
        tab[i], tab[1] = tab[1], tab[i]
        tab[0] -= 1
        heapify(tab, 1)


# kolejka priorytetowa, q[0] przechowuje ilość elementów
def getmax(q):
    if q[0] == 0:
        sys.exit()
    res = q[1]
    q[1] = q[q[0]]
    q[0] -= 1
    heapify(q, 1)
    return res


def insert(q, x):
    if q[0] == len(q) - 1:
        sys.exit()
    q[0] += 1
    i = q[0]
    q[i] = x
    while i > 1 and q[i] > q[i//2]:
        q[i], q[i//2] = q[i//2], q[i]
        i //= 2


# mergowanie k tablic z pomocą kopca
class Element:
    def __init__(self):
        self.val = None
        self.lindex = None
        self.lpos = None


def insertMinE(q, x):
    if q[0] == len(q) - 1:
        sys.exit()
    q[0] += 1
    i = q[0]
    q[i] = x
    while i > 1 and q[i].val < q[i//2].val:
        q[i], q[i//2] = q[i//2], q[i]
        i //= 2


def heapifyMinE(tab, root):
    largest = root
    left = 2*root
    right = 2*root+1

    if left <= tab[0] and tab[left].val < tab[largest].val:
        largest = left

    if right <= tab[0] and tab[right].val < tab[largest].val:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapifyMinE(tab, largest)


def mergek(lista):
    heap = [0]*(len(lista)+1)
    for i, val in enumerate(lista):
        if len(val) == 0:
            break
        el = Element()
        el.val = val[0]
        el.lindex = i
        el.lpos = 0
        insertMinE(heap, el)

    tab = []
    while heap[0] != 0:
        tab.append(heap[1].val)
        heap[1].lpos += 1
        if heap[1].lpos < len(lista[heap[1].lindex]):
            heap[1].val = lista[heap[1].lindex][heap[1].lpos]
        else:
            heap[1] = heap[heap[0]]
            heap[0] -= 1
        heapifyMinE(heap, 1)
    return tab


# struktura danych z getMedian() i insert(x) w O(logn)
def insertMin(q, x):
    if q[0] == len(q) - 1:
        q.append(0)
        q[0] += 1
    i = q[0]
    q[i] = x
    while i > 1 and q[i] < q[i//2]:
        q[i], q[i//2] = q[i//2], q[i]
        i //= 2


def insertMax(q, x):
    if q[0] == len(q) - 1:
        q.append(0)
        q[0] += 1
    i = q[0]
    q[i] = x
    while i > 1 and q[i] > q[i // 2]:
        q[i], q[i // 2] = q[i // 2], q[i]
        i //= 2


class DoubleHeap:
    def __init__(self):
        self.minheap = [0]
        self.maxheap = [0]
        self.median = None


def getMedian(dheap: DoubleHeap):
    if dheap.median is None:
        return (dheap.minheap[1] + dheap.maxheap[1])/2
    else:
        return dheap.median


def insertToDH(dheap: DoubleHeap, x):
    if dheap.minheap[0] == 0:
        dheap.minheap.append(x)
        dheap.minheap[0] += 1
        dheap.median = x
    elif dheap.maxheap[0] == 0:
        if x < (x+dheap.minheap[1])/2:
            dheap.maxheap.append(x)
        else:
            dheap.maxheap.append(dheap.minheap[1])
            dheap.minheap[1] = x
        dheap.median = None
        dheap.maxheap[0] += 1
    else:
        if dheap.median is None:
            if dheap.minheap[1] > x > dheap.maxheap[1]:
                dheap.median = x
            elif dheap.minheap[1] > dheap.maxheap[1] > x:
                dheap.median = dheap.maxheap[1]
                dheap.maxheap[1] = x
                heapify(dheap.maxheap, 1)
            else:
                dheap.median = dheap.minheap[1]
                dheap.minheap[1] = x
                heapifyMin(dheap.minheap, 1)
        else:
            insertMax(dheap.maxheap, min(x, dheap.median))
            insertMin(dheap.minheap, max(x, dheap.median))
            dheap.median = None


# getMin() i getMax() w log(n)
class DualHeap:
    def __init__(self):
        self.minheap = [0]
        self.maxheap = [0]


def heapifyMinD(minq, maxq, root):
    largest = root
    left = 2*root
    right = 2*root+1

    if left <= minq[0] and minq[left][0] < minq[largest][0]:
        largest = left

    if right <= minq[0] and minq[right][0] < minq[largest][0]:
        largest = right

    if largest != root:
        minq[root], minq[largest] = minq[largest], minq[root]
        maxq[minq[root][1]][1] = root
        maxq[minq[largest][1]][1] = largest
        heapifyMinD(minq, maxq, largest)


def heapifyMaxD(minq, maxq, root):
    largest = root
    left = 2*root
    right = 2*root+1

    if left <= minq[0] and minq[left][0] > minq[largest][0]:
        largest = left

    if right <= minq[0] and minq[right][0] > minq[largest][0]:
        largest = right

    if largest != root:
        minq[root], minq[largest] = minq[largest], minq[root]
        maxq[minq[root][1]][1] = root
        maxq[minq[largest][1]][1] = largest
        heapifyMaxD(minq, maxq, largest)


def insertt(q: DualHeap, x):
    q.minheap.append(0)
    q.maxheap.append(0)
    q.minheap[0] += 1
    q.maxheap[0] += 1

    i = q.minheap[0]
    j = q.maxheap[0]
    q.minheap[i] = [x, j]
    q.maxheap[j] = [x, i]

    fixMinHeap(q.minheap, q.maxheap, i)
    fixMaxHeap(q.maxheap, q.minheap, j)


def fixMinHeap(minheap, maxheap, i):
    while i > 1 and minheap[i][0] < minheap[i//2][0]:
        maxheap[minheap[i][1]][1] = i//2
        maxheap[minheap[i//2][1]][1] = i
        minheap[i], minheap[i//2] = minheap[i//2], minheap[i]
        i //= 2


def fixMaxHeap(maxheap, minheap, j):
    while j > 1 and maxheap[j][0] > maxheap[j//2][0]:
        minheap[maxheap[j][1]][1] = j//2
        minheap[maxheap[j//2][1]][1] = j
        maxheap[j], maxheap[j//2] = maxheap[j//2], maxheap[j]
        j //= 2


def getMin(q: DualHeap):
    if q.minheap[0] == 0:
        return None
    mini = q.minheap[1]
    q.minheap[1] = q.minheap[q.minheap[0]]
    q.maxheap[q.minheap[1][1]][1] = 1
    q.minheap.pop()
    q.minheap[0] -= 1
    heapifyMinD(q.minheap, q.maxheap, 1)

    if mini[1] != q.maxheap[0]:
        q.maxheap[mini[1]] = q.maxheap[q.maxheap[0]]
        q.minheap[q.maxheap[mini[1]][1]][1] = mini[1]
    q.maxheap[0] -= 1
    q.maxheap.pop()

    if mini[1] <= q.maxheap[0]:
        fixMaxHeap(q.maxheap, q.minheap, mini[1])

    return mini[0]


def getMax(q: DualHeap):
    if q.maxheap[0] == 0:
        return None
    maxi = q.maxheap[1]
    q.maxheap[1] = q.maxheap[q.maxheap[0]]
    q.minheap[q.maxheap[1][1]][1] = 1
    q.maxheap.pop()
    q.maxheap[0] -= 1
    heapifyMaxD(q.maxheap, q.minheap, 1)

    if maxi[1] != q.minheap[0]:
        q.minheap[maxi[1]] = q.minheap[q.minheap[0]]
        q.maxheap[q.minheap[maxi[1]][1]][1] = maxi[1]
    q.minheap[0] -= 1
    q.minheap.pop()

    if maxi[1] <= q.minheap[0]:
        fixMinHeap(q.minheap, q.maxheap, maxi[1])

    return maxi[0]


tablica = [random.randint(1, 100) for i in range(10)]
tablica[0] = len(tablica) - 1
heapsort(tablica)
print(tablica)

lista = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
lista = mergek(lista)
print(lista)

# dheap = DoubleHeap()
# while True:
#     insertToDH(dheap, int(input("Podaj liczbę")))
#     print(getMedian(dheap))

siema = DualHeap()
insertt(siema, 3)
insertt(siema, 1)
insertt(siema, 2)
insertt(siema, 5)
getMin(siema)
getMin(siema)
getMax(siema)
getMax(siema)
getMax(siema)
print(siema.maxheap)
print(siema.minheap)


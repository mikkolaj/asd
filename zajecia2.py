import random


def quicksort(tab, left, right):
    if right <= left:
        return
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


def heapify(tab, size, root):
    largest = root
    left = 2*root+1
    right = 2*root+2

    if left < size and tab[left] > tab[largest]:
        largest = left

    if right < size and tab[right] > tab[largest]:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapify(tab, size, largest)


def heapsort(tab):
    size = len(tab)

    for i in range(size//2, -1, -1):
        heapify(tab, size, i)

    for i in range(size-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i, 0)


tablica = [random.randint(1, 100) for i in range(10)]
heapsort(tablica)
print(tablica)


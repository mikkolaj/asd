import random
posortowana = list(range(1, 17, 2))
losowa = []

for i in range(10):
    losowa.append(random.randint(1, 100))


def bsearch(tab, val):
    left = 0
    right = len(tab)-1
    while left <= right:
        mid = (left + right)//2
        if tab[mid] > val:
            right = mid - 1
        elif tab[mid] < val:
            left = mid + 1
        else:
            return mid
    return -1


def tsearch(tab, val):
    left = 0
    right = len(tab) - 1
    while left <= right:
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3
        if tab[mid1] == val:
            return mid1
        if tab[mid2] == val:
            return mid2
        if tab[mid1] > val:
            right = mid1 - 1
        elif tab[mid2] < val:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1


def bubblesort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1-j):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


kolory = [1, 1, 3, 2, 2, 2, 4, 4, 3, 2, 1]


# funkcja zwraca długość najkrótszego łańcucha zawierającego 4 różne kolory
def clen(tab, n):
    p = -1
    k = 0
    mindlug = float('inf')
    indeksy = None
    ileliczb = n*[0]
    while p < len(tab):
        if brakuje(ileliczb):
            if p < len(tab) - 1:
                p += 1
                ileliczb[tab[p]-1] += 1
            else:
                break
        else:
            if p - k + 1 < mindlug:
                mindlug = p - k + 1
                indeksy = (p, k)
            ileliczb[tab[k]-1] -= 1
            k += 1
    return indeksy


def brakuje(tab):
    for i in tab:
        if i == 0:
            return True
    return False


def swaporder(tab, p, k):
    n = k - p + 1
    for i in range(n//2):
        tab[p+i], tab[k-i] = tab[k-i], tab[p+i]


def movelast(tab, n):
    swaporder(tab, len(tab)-n, len(tab)-1)
    swaporder(tab, 0, len(tab)-n-1)
    swaporder(tab, 0, len(tab)-1)


def indicesofsum(tab, sm):
    i = 0
    j = len(tab) - 1
    tsum = tab[i] + tab[j]
    while i != j:
        if tsum == sm:
            return i, j
        elif tsum > sm:
            j -= 1
            tsum = tab[i] + tab[j]
        else:
            i += 1
            tsum = tab[i] + tab[j]
    return None


def morethanhalf(tab):
    licznik = 1
    akt = tab[0]
    for i in range(1, len(tab)):
        if tab[i] == akt:
            licznik += 1
        else:
            licznik -= 1
            if licznik == 0:
                akt = tab[i]
                licznik += 1
    licznik = 0
    for i in tab:
        if i == akt:
            licznik += 1
    if licznik > len(tab)/2:
        return True
    else:
        return False


def minmax(tab):
    minim, maxim = (tab[1], tab[0]) if tab[0] > tab[1] else (tab[0], tab[1])
    i, j = 2, 3
    while j < len(tab):
        if tab[i] < tab[j]:
            if tab[i] < minim:
                minim = tab[i]
            if tab[j] > maxim:
                maxim = tab[j]
        else:
            if tab[j] < minim:
                minim = tab[j]
            if tab[i] > maxim:
                maxim = tab[j]
        i += 2
        j += 2
    if len(tab) % 2 != 0:
        if tab[i] > maxim:
            maxim = tab[i]
        else:
            if tab[i] < minim:
                minim = tab[i]
    return minim, maxim


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def addBeg(head, node):
    node.next = head
    return node


def addEnd(head, nowy):
    if head is None:
        return nowy
    else:
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = nowy
        return head


def printList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print("")


def getMin(head):
    wart = Node()
    wart.next = head
    befmin = wart
    tmp = wart
    while tmp.next is not None:
        if tmp.next.val < befmin.next.val:
            befmin = tmp
        tmp = tmp.next
    tmp = befmin.next
    if befmin.next is not None:
        befmin.next = befmin.next.next
    return tmp, wart.next


def sortList(head):
    wynik = Node()
    while head is not None:
        minimum, head = getMin(head)
        minimum.next = None
        addEnd(wynik, minimum)
    return wynik.next


beg = None
for i in range(10):
    nowy = Node()
    nowy.val = random.randint(1, 100)
    beg = addEnd(beg, nowy)

printList(beg)
minimum, beg = getMin(beg)
print("Minimum:", minimum.val, "Lista:")
printList(beg)
beg = sortList(beg)
printList(beg)


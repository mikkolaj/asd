import random


def partition(tab, left, right):
    mid = (left+right)//2
    pivot = tab[mid]
    while left <= right:
        while tab[left] < pivot:
            left += 1
        while tab[right] > pivot:
            right -= 1
        if left <= right:
            if right == mid:
                mid = left
            elif left == mid:
                mid = right
            tab[left], tab[right] = tab[right], tab[left]
            left += 1
            right -= 1
    return mid


def partition2(tab, left, right, val):
    for i in range(len(tab)):
        if tab[i] == val:
            val = i
            break
    pivot = tab[val]
    while left <= right:
        while tab[left] < pivot:
            left += 1
        while tab[right] > pivot:
            right -= 1
        if left <= right:
            if left == val:
                val = right
            elif right == val:
                val = left
            tab[left], tab[right] = tab[right], tab[left]
            left += 1
            right -= 1
    return val


def select(tab, l, r, i):
    if l == r:
        return tab[l]
    mid = partition(tab, l, r)
    k = mid - l + 1
    if i == k:
        return tab[mid]
    elif k < i:
        return select(tab, mid+1, r, i-k)
    else:
        return select(tab, l, mid-1, i)


def select2(tab, l, r, i):
    if l == r:
        return tab[l]
    mid = partition2(tab, l, r, mediana(tab, l, r))
    k = mid - l + 1
    if i == k:
        return tab[mid]
    elif k < i:
        return select2(tab, mid+1, r, i-k)
    else:
        return select2(tab, l, mid-1, i)


def inssort(tab, l, r):
    for i in range(l+1, r+1):
        ref = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > ref:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = ref


def mediana(tab, l, r):
    med = []
    for i in range(l, r+1, 5):
        j = i + 4
        if j > r:
            j = r
        inssort(tab, i, j)
        med.append(tab[(i+j)//2])
    if len(med) == 1:
        return med[0]
    else:
        return mediana(med, 0, len(med)-1)


def cyfra(x, i):
    for j in range(i):
        wyn = x % 10
        x //= 10
    return wyn


def radixsort(tab, k):
    for i in range(k):
        temp = [[] for s in range(10)]
        for j in tab:
            temp[cyfra(j, i+1)].append(j)
        h = 0
        for j in temp:
            for f in j:
                tab[h] = f
                h += 1


def bucketsort(tab, k):
    maks = max(tab) + 1
    b = [[] for i in range(k)]
    for el in tab:
        b[int(el/maks*k)].append(el)
    for i in range(k):
        inssort(b[i], 0, len(b[i])-1)
    res = []
    for i in range(k):
        res.extend(b[i])
    return res


def trisort(tab):
    if len(tab) > 1:
        l = []
        e = []
        m = []
        ref = tab[0]
        for i in tab:
            if i < ref:
                l.append(i)
            elif i > ref:
                m.append(i)
            else:
                e.append(i)
        l = trisort(l)
        m = trisort(m)
        tab = []
        tab.extend(l)
        tab.extend(e)
        tab.extend(m)
    return tab


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def create(l):
    if len(l) == 0:
        return [None, None]
    first = Node()
    first.val = l[0]
    last = first
    for i in range(1, len(l)):
        new = Node()
        new.val = l[i]
        last.next = new
        last = new
    return [first, last]


def concat(l, r):
    if l[0] is None:
        return r
    if r[0] is None:
        return l
    l[1].next = r[0]
    l[1] = r[1]
    return l


def empty(l):
    return l[0] is None


def get(l):
    res = l[0]
    l[0] = l[0].next
    res.next = None
    return res


def append(l, el):
    if l[0] is None:
        l[0] = el
    else:
        l[1].next = el
    l[1] = el


def printlist(l):
    s = l[0]
    while s is not None:
        print(s.val, end=" ")
        s = s.next
    print("")


def quicksort(l):
    if empty(l) or l[0] == l[1]:
        return l
    x = l[0].val
    lt = [None, None]
    eq = [None, None]
    gt = [None, None]
    while not empty(l):
        y = get(l)
        if y.val > x:
            append(gt, y)
        elif y.val < x:
            append(lt, y)
        else:
            append(eq, y)
    return concat(concat(quicksort(lt), eq), quicksort(gt))


l1 = [2]
ll1 = create(l1)
printlist(ll1)
ll2 = quicksort(ll1)
printlist(ll2)
print(select2([10, 29, 10, 19, 11, 7, 12, 17, 3, 2, 5], 0, 10, 3))
print(select2([2, 3, 5, 7, 10, 10, 11, 12, 17, 19, 29], 0, 10, 3))

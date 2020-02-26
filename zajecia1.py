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
        for j in range(len(tab)-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


def quicksort(tab, left, right):
    if right <= left:
        return
    mid = tab[(left+right)//2]
    i = left
    j = right
    while True:
        while tab[i] < mid:
            i += 1
        while tab[j] > mid:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
        else:
            break
    if j > left:
        quicksort(tab, left, j)
    if i < right:
        quicksort(tab, i, right)


print(posortowana)
print(tsearch(posortowana, 1))

print(losowa)
quicksort(losowa, 0, len(losowa)-1)
print(losowa)


def iquicksort(tab, left, right):
    stack = [0]*len(tab)
    top = 0
    stack[top] = left
    top += 1
    stack[top] = right
    while top > 0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1
        mid = partition(tab, left, right)
        if mid - 1 > left:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = mid - 1
        if mid + 1 < right:
            top += 1
            stack[top] = mid + 1
            top += 1
            stack[top] = right


def iquicksort(A, i, j):
    S = Stack()
    S.push(i)
    S.push(j)
    while not S.is_empty():
        right = S.pop()
        left = S.pop()
        mid = partition(A, i, j)
        if mid - 1 > left:
            S.push(i)
            S.push(mid - 1)
        if mid + 1 < right:
            S.push(mid + 1)
            S.push(right)


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


def countingsort(tab, maks):
    temp = [0]*(maks+1)
    for i in tab:
        temp[i] += 1
    el = 0
    for i in range(len(temp)):
        while temp[i] > 0:
            tab[el] = i
            temp[i] -= 1
            el += 1


def countingsort(tab):
    n = len(tab)
    k = max(tab)
    counts = [0]*(k+1)
    output = [0]*n

    for i in tab:
        counts[i] += 1

    for i in range(1, k+1):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        output[counts[tab[i]]-1] = tab[i]
        counts[tab[i]] -= 1

    return output


tab = [10, 29, 10, 19, 11, 7, 12, 17, 3, 2, 5]
# iquicksort(tab, 0, len(tab)-1)
tab = countingsort(tab)
print(tab)

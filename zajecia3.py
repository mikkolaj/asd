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


def partition(tab, left, right):
    mid = (left+right)//2
    while left <= right:
        while tab[left] < tab[mid]:
            left += 1
        while tab[right] > tab[mid]:
            right -= 1
        if left <= right:
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


tab = [10, 29, 10, 19, 11, 7, 12, 17, 3, 2, 5]
iquicksort(tab, 0, len(tab)-1)
# countingsort(tab, 29)
print(tab)

def position(p1, p2, x, y):
    prod = (p1[0]-x)*(p2[1]-y) - (p1[1]-y)*(p2[0]-x)
    if prod == 0:
        return 1
    elif prod > 0:
        return 2
    return 0


def area(points: list):
    sum = 0
    for i in range(1, len(points)):
        sum -= (points[i][0] - points[i-1][0])*(points[i][1] + points[i-1][1])/2
    return sum


def quicksort(tab, left, right, point):
    mid = tab[(left+right)//2]
    i = left
    j = right
    while i <= j:
        while position(tab[i], mid, point[0], point[1]) == 2:
            i += 1
        while position(tab[j], mid, point[0], point[1]) == 0:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
    if j > left:
        quicksort(tab, left, j, point)
    if i < right:
        quicksort(tab, i, right, point)


# Graham
def otoczka(points: list):
    point = points[0]
    for i in points:
        if i[1] < point[1]:
            point = i
    points.remove(point)
    quicksort(points, 0, len(points)-1, point)
    points.insert(0, point)
    stack = [points[0], points[1], points[2]]

    for i in range(3, len(points)):
        n = len(stack)-1
        while position(points[i], stack[n], stack[n-1][0], stack[n-1][1]) == 2:
            stack.pop()
            n -= 1
        stack.append(points[i])

    return stack


points = [(6, 2), (8, 4), (10, 3), (6, 6), (7, 6), (8, 8), (2, 10)]

print(otoczka(points))



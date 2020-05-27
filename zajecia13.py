class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.leaf = False
        self.intervals = []
        self.height = 0
        self.span = None


def printChildrenFirst(tree: Node):
    if tree is None:
        print("Drzewo puste")
        return
    children = [tree]
    while children:
        newchildren = []
        for i in children:
            print(i.val, i.span, end=" ")
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        print("")
        children = newchildren


def construct(points, i, j):
    if j >= i:
        node = Node()
        mid = (i+j)//2
        node.val = points[mid]
        node.left = construct(points, i, mid-1)
        node.left.parent = node
        node.right = construct(points, mid+1, j)
        node.left.parent = node
        return node
    return Node()


def span(node, left, right):
    if node is not None:
        node.span = (left, right)
        span(node.left, left, node.val)
        span(node.right, node.val, right)


def findmax(node, i, j):
    if node.leaf is False:
        if j <= node.val:
            return findmax(node.left, i, j)
        elif i >= node.val:
            return findmax(node.right, i, j)
        else:
            return max(findmax(node.left, i, j), findmax(node.right, i, j))
    return node.height


def bricks(intervals):
    points = []
    for i, j in intervals:
        points.extend([i, j])
    points = list(set(points))
    points.sort()
    print(points)
    node = construct(points, 0, len(points) - 1)
    span(node, float("-inf"), float("inf"))
    printChildrenFirst(node)
    node.leaf = True
    for i, j in intervals:
        maks = findmax(node, i, j) + 1






bricks( [ (1, 3), (2, 5), (0, 3), (8, 9), (4, 6)] )
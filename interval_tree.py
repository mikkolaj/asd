class Node:
    def __init__(self, interval, mid, val):
        self.interval = interval
        self.mid = mid
        self.val = val
        self.left = None
        self.right = None


class IntervalSums:
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2

        # tworzymy drzewo o przedziałach jednostkowych od 0 do najbliższej potęgi dwójki
        # większej od n, wtedy będzie dobrze zbalansowane
        root = Node((0, size), (0 + size)/2, 0)
        self.root = root

        def build(node):
            if node.interval[1] - node.interval[0] == 1:
                return
            left = Node((node.interval[0], node.mid), (node.interval[0] + node.mid)/2, 0)
            node.left = left
            build(node.left)
            right = Node((node.mid, node.interval[1]), (node.mid + node.interval[1])/2, 0)
            node.right = right
            build(node.right)

        build(self.root)

    def set(self, i, val):
        def correct(node, j, v):
            if node.interval[1] - node.interval[0] == 1:
                node.val = v
                return
            if i < node.mid:
                correct(node.left, j, v)
            else:
                correct(node.right, j, v)
            node.val = node.left.val + node.right.val
        correct(self.root, i, val)

    def interval(self, i, j):
        def Sum(node, l, r, s):
            if l <= node.interval[0] and r >= node.interval[1]:
                return node.val
            if l < node.mid < r:
                s += (Sum(node.left, l, r, s) + Sum(node.right, l, r, s))
            elif l < node.mid:
                s += Sum(node.left, l, r, s)
            elif r > node.mid:
                s += Sum(node.right, l, r, s)
            return s

        return Sum(self.root, i, j + 1, 0)


IS = IntervalSums(3)
IS.set(2, 6)
IS.set(0, 10)
IS.set(1, 4)
IS.set(0, 9)
print(IS.interval(0, 1), IS.interval(1, 2), IS.interval(0, 2))
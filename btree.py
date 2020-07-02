class Node:
    def __init__(self):
        self.values = []
        self.next = []
        self.parent = None


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def devastateNode(self, node: Node):
        mid = (3*self.t - 2)//2 - 1
        if node == self.root:
            left = Node()
            right = Node()
            left.values = node.values[:mid]
            left.next = node.next[:mid+1]
            left.parent = node
            for i in left.next:
                i.parent = left
            right.values = node.values[mid+1:]
            right.next = node.next[mid+1:]
            right.parent = node
            for i in right.next:
                i.parent = right
            node.values = [node.values[mid]]
            node.next = [left, right]
        else:
            right = Node()
            right.values = node.values[mid+1:]
            right.next = node.next[mid+1:]
            right.parent = node.parent
            val = node.values[mid]
            node.values = node.values[:mid]
            node.next = node.next[:mid+1]
            for i in range(len(node.parent.values) + 1):
                if i == len(node.parent.values) or val < node.parent.values[i]:
                    node.parent.values.insert(i, val)
                    node.parent.next.insert(i+1, right)
                    break

    def insert(self, val, node, allowdevastation):
        if allowdevastation and len(node.values) == 2 * self.t - 1:
            self.devastateNode(node)
            if node.parent is not None:
                self.insert(val, node.parent, False)
            else:
                self.insert(val, node, False)
        elif len(node.next) == 0:
            for i in range(len(node.values) + 1):
                if i == len(node.values) or val < node.values[i]:
                    node.values.insert(i, val)
                    break
        else:
            for i in range(len(node.values) + 1):
                if i == len(node.values) or val < node.values[i]:
                    self.insert(val, node.next[i], True)
                    break

    def printChildrenFirst(self):
        if self.root is None:
            print("Drzewo puste")
            return
        children = [tree.root]
        while children:
            newchildren = []
            for i in children:
                print("|", end=" ")
                for j in i.values:
                    print(j, end=" ")
                for j in i.next:
                    newchildren.append(j)
            print("|")
            children = newchildren


def printDepthFirst(tree: Node):
    if tree is None:
        print("Drzewo puste")
        return
    printDepthFirst(tree.left)
    print(tree.value)
    printDepthFirst(tree.right)


def insert(tree: Node, val):
    if tree is None:
        tree = Node()
        tree.value = val
    elif val < tree.value:
        tree.left = insert(tree.left, val)
    elif val > tree.value:
        tree.right = insert(tree.right, val)
    return tree


def insert2(tree: Node, val):
    if tree.value is None:
        tree.value = val
    elif val < tree.value:
        tree.left = tree.left or Node()
        insert(tree.left, val)
    elif val > tree.value:
        tree.right = tree.right or Node()
        insert(tree.right, val)


def delete(tree: Node, val, parent):
    res = tree
    while tree is not None and tree.value != val:
        if val < tree.value:
            parent = tree
            tree = tree.left
        elif val > tree.value:
            parent = tree
            tree = tree.right

    if tree is not None:
        if tree.left is None and tree.right is None:
            if parent is None:
                return None
            if parent.left == tree:
                parent.left = None
            else:
                parent.right = None
        elif tree.left is not None and tree.right is not None:
            child = tree.right
            childparent = tree
            while child.left is not None:
                childparent = child
                child = child.left
            tree.value = child.value
            delete(child, child.value, childparent)
        else:
            if parent is None:
                return tree.left or tree.right
            if tree == parent.left:
                parent.left = tree.left or tree.right
            else:
                parent.right = tree.left or tree.right

    return res


tree = BTree(2)
tree.root = Node()
tree.root.values = [2, 10]
left = Node()
left.values = [0, 1]
left.parent = tree.root
mid = Node()
mid.values = [5, 8]
mid.parent = tree.root
right = Node()
right.values = [15, 16, 17]
right.parent = tree.root
tree.root.next = [left, mid, right]

tree.printChildrenFirst()
tree.insert(16.5, tree.root, True)
tree.printChildrenFirst()
tree.insert(17.5, tree.root, True)
tree.printChildrenFirst()
tree.insert(18.5, tree.root, True)
tree.printChildrenFirst()
tree.insert(9, tree.root, True)
tree.printChildrenFirst()
tree.insert(9.5, tree.root, True)
tree.printChildrenFirst()



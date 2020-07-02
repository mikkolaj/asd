class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def printDepthFirst(tree: Node):
    if tree is None:
        print("Drzewo puste")
        return
    printDepthFirst(tree.left)
    print(tree.value)
    printDepthFirst(tree.right)


def printChildrenFirst(tree: Node):
    if tree is None:
        print("Drzewo puste")
        return
    children = [tree]
    while children:
        newchildren = []
        for i in children:
            print(i.value, end=" ")
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        print("")
        children = newchildren


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


tree = None
tree = insert(tree, 8)
tree = insert(tree, 4)
tree = insert(tree, 12)
tree = insert(tree, 2)
tree = insert(tree, 6)
tree = insert(tree, 1)
tree = insert(tree, 3)
tree = insert(tree, 5)
tree = insert(tree, 7)
tree = insert(tree, 10)
tree = insert(tree, 9)
tree = insert(tree, 11)
tree = insert(tree, 14)
tree = insert(tree, 13)
tree = insert(tree, 15)

tree = delete(tree, 12, None)
tree = delete(tree, 6, None)
tree = delete(tree, 3, None)
printChildrenFirst(tree)

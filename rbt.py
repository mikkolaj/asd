class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.black = True


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
            print(i.value)
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        children = newchildren


def insert(tree: Node, val):
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
            if parent.left and parent.left == tree:
                parent.left = None
            else:
                parent.right = None
        if tree.left is not None and tree.right is not None:
            child = tree.right
            childparent = tree
            while child.left is not None:
                child = child.left
                parent = child
            tree.value = child.value
            if childparent != tree:
                childparent.left = None
            else:
                tree.right = None
    return res


tree = Node()
insert(tree, 2)
insert(tree, 1)
insert(tree, 3)
tree = delete(tree, 2, None)
tree = delete(tree, 1, None)
tree = delete(tree, 3, None)
printChildrenFirst(tree)

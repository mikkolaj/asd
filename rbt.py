class RBNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.black = True
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None


def insert(node: RBTree, x):
    new = RBNode(x)
    if node.root is None:
        node.root = new
        return
    current = node.root
    parent = None
    while current is not None:
        parent = current
        if x < current.value:
            current = current.left
        elif x > current.value:
            current = current.right
        else:
            return
    new.parent = parent
    new.black = False
    if x < parent.value:
        parent.left = new
    else:
        parent.right = new
    fixRBTree(new, node)


def fixRBTree(node: RBNode, tree: RBTree):
    while node.parent is not None and not node.parent.black:
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if not uncle.black:
                node.parent.black = uncle.black = True
                node.parent.parent.black = False
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    rotateLeft(node.parent, tree)
                    node = node.left
                node.parent.black = True
                node.parent.parent.black = False
                rotateRight(node.parent.parent, tree)
        else:
            uncle = node.parent.parent.left
            if not uncle.black:
                node.parent.black = uncle.black = True
                node.parent.parent.black = False
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    rotateRight(node.parent, tree)
                    node = node.right
                node.parent.black = True
                node.parent.parent.black = False
                rotateLeft(node.parent.parent, tree)
    tree.root.black = True


def rotateLeft(node, tree):
    child = node.right
    node.right = child.left
    if child.left is not None:
        child.left.parent = node
    child.left = node
    if node.parent is None:
        tree.root = child
    else:
        if node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
    node.parent = child


def rotateRight(node, tree):
    child = node.left
    node.left = child.right
    if child.right is not None:
        child.right.parent = node
    child.right = node
    if node.parent is None:
        tree.root = child
    else:
        if node == node.parent.right:
            node.parent.right = child
        else:
            node.parent.left = child
    node.parent = child


def printDepthFirst(node: RBNode):
    if node is None:
        print("Drzewo puste")
        return
    printDepthFirst(node.left)
    print(node.value)
    printDepthFirst(node.right)


def printChildrenFirst(node: RBNode):
    if node is None:
        print("Drzewo puste")
        return
    children = [node]
    while children:
        newchildren = []
        for i in children:
            print(i.value)
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        children = newchildren


# def delete(tree: Node, val, parent):
#     res = tree
#     while tree is not None and tree.value != val:
#         if val < tree.value:
#             parent = tree
#             tree = tree.left
#         elif val > tree.value:
#             parent = tree
#             tree = tree.right
#
#     if tree is not None:
#         if tree.left is None and tree.right is None:
#             if parent is None:
#                 return None
#             if parent.left and parent.left == tree:
#                 parent.left = None
#             else:
#                 parent.right = None
#         if tree.left is not None and tree.right is not None:
#             child = tree.right
#             childparent = tree
#             while child.left is not None:
#                 child = child.left
#                 parent = child
#             tree.value = child.value
#             if childparent != tree:
#                 childparent.left = None
#             else:
#                 tree.right = None
#     return res


tree = RBTree()
insert(tree, 2)
insert(tree, 1)
insert(tree, 3)
printChildrenFirst(tree.root)

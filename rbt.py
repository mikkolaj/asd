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


def rotateLeft(tree, node):
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
    child.parent = node.parent
    node.parent = child


def rotateRight(tree, node):
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
    child.parent = node.parent
    node.parent = child


def printDepthFirst(node: RBNode):
    if node is None:
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
            print(i.value, end=" ")
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        print("")
        children = newchildren


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
            if uncle is not None and not uncle.black:
                node.parent.black = uncle.black = True
                node.parent.parent.black = False
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    rotateLeft(tree, node.parent)
                    node = node.left
                if node == node.parent.left:
                    node.parent.black = True
                    node.parent.parent.black = False
                    rotateRight(tree, node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle is not None and not uncle.black:
                node.parent.black = uncle.black = True
                node.parent.parent.black = False
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    rotateRight(tree, node.parent)
                    node = node.right
                if node == node.parent.right:
                    node.parent.black = True
                    node.parent.parent.black = False
                    rotateLeft(tree, node.parent.parent)
    tree.root.black = True


def delete(tree: RBTree, node: RBNode, val):
    while node is not None and node.value != val:
        if val < node.value:
            node = node.left
        elif val > node.value:
            node = node.right
    if node is not None:
        if node.left is not None and node.right is not None:
            succesor = findSuccesor(node.right)
            node.value = succesor.value
            print(succesor.value)
            delete(tree, succesor, succesor.value)
        elif node.left is None and node.right is None:
            if not node.black:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            elif node.black and node == tree.root:
                tree.root = None
            else:
                deleteCase1(tree, node)
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None

        else:  # tylko jedno dziecko nie jest NULL liściem
            child = node.left or node.right
            node.value = child.value
            node.black = True
            node.left = child.left
            node.right = child.right


def deleteCase1(tree, node):
    if node != tree.root:
        deleteCase2(tree, node)


def deleteCase2(tree, node):
    if node == node.parent.left:
        sibling = node.parent.right
        if node.parent.black and not sibling.black:
            node.parent.black = False
            sibling.black = True
            rotateLeft(tree, node.parent)
    else:
        sibling = node.parent.left
        if node.parent.black and not sibling.black:
            node.parent.black = False
            sibling.black = True
            rotateRight(tree, node.parent)
    deleteCase3(tree, node)


def deleteCase3(tree, node):
    if node == node.parent.left:
        sibling = node.parent.right
    else:
        sibling = node.parent.left
    if node.parent.black and sibling.black and (sibling.left is None or sibling.left.black) and \
            (sibling.right is None or sibling.right.black):
        sibling.black = False
        deleteCase1(tree, node.parent)
    else:
        deleteCase4(tree, node)


def deleteCase4(tree, node):
    if node == node.parent.left:
        sibling = node.parent.right
    else:
        sibling = node.parent.left
    if not node.parent.black and sibling.black and (sibling.left is None or sibling.left.black) and \
            (sibling.right is None or sibling.right.black):
        node.parent.black = True
        sibling.black = False
    else:
        deleteCase5(tree, node)


def deleteCase5(tree, node):
    if node == node.parent.left:
        sibling = node.parent.right
        if sibling.black and sibling.left is not None and not sibling.left.black and (sibling.right is None or
                                                                                      sibling.right.black):
            sibling.left.black = True
            sibling.black = False
            rotateRight(tree, sibling)
    else:
        sibling = node.parent.left
        if sibling.black and sibling.right is not None and not sibling.right.black and (sibling.left is None or
                                                                                        sibling.left.black):
            sibling.right.black = True
            sibling.black = False
            rotateLeft(tree, sibling)
    deleteCase6(tree, node)


def deleteCase6(tree, node):
    if node == node.parent.left:
        sibling = node.parent.right
        if sibling.black and sibling.right is not None and not sibling.right.black:
            sibling.black = node.parent.black
            node.parent.black = True
            sibling.right.black = True
            rotateLeft(tree, node.parent)
    else:
        sibling = node.parent.left
        if sibling.black and sibling.left is not None and not sibling.left.black:
            sibling.black = node.parent.black
            node.parent.black = True
            sibling.left.black = True
            rotateRight(tree, node.parent)


def findSuccesor(node: RBNode):
    while node.left is not None:
        node = node.left
    return node


tree = RBTree()
for i in range(100):
    insert(tree, i)
printChildrenFirst(tree.root)
for i in range(100, -1, -1):
    delete(tree, tree.root, i)
printChildrenFirst(tree.root)


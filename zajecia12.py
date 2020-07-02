class BSTNode:
    def __init__(self, key, value):
        self.left  = None
        self.right = None   # pola parent nie ma -- nie jest w tym zadaniu potrzebne
        self.key   = key
        self.value = value


class BSTDict:
    def __init__( self ):
        self.tree = None    # tu powinien być korzeń drzewa# gdy slownik nie jest pusty

    def find_elem(self, key, head):  # nie wkładamy tych samych elementów
        prev = None
        while head is not None:
            temp = head
            if key > head.key:
                head = head.right
            elif key < head.key:
                head = head.left
            else:
                return prev, head
            prev = temp
        return prev, head

    def insert( self, key, value ):
        # wstaw wartość value pod klucz key (jeśli klucz key
        # już istnieje, to podmień przechowywaną wartość
        # value
        new = BSTNode(key, value)
        head = self.tree
        if head is None:
            self.tree = new
            return
        prev, _ = self.find_elem(key, head)
        if key > prev.key:
            prev.right = new
        else:
            prev.left = new

    def find_succ(self, head):
        prev = head
        head = head.right
        while head.left is not None:
            prev = head
            head = head.left
        return prev, head

    def remove(self, key, start=None):
        if start is None:
            start = self.tree
        prev, head = self.find_elem(key, start)

        if head.left is None and head.right is None:
            if prev is not None:
                if head == prev.left:
                    prev.left = None
                else:
                    prev.right = None
            else:
                self.tree = None
        elif (head.right is None and head.left is not None) or (head.right is not None and head.left is None):
            if prev is not None:
                if head == prev.left:
                    prev.left = head.left or head.right
                else:
                    prev.right = head.left or head.right
            else:
                self.tree = head.left or head.right
        else:
            prev, succ = self.find_succ(head)
            skey, sval = succ.key, succ.value
            self.remove(skey, prev)
            head.key, head.val = skey, sval


def printChildrenFirst(tree: BSTNode):
    if tree is None:
        print("Drzewo puste")
        return
    children = [tree]
    while children:
        newchildren = []
        for i in children:
            print(i.key, i.value, end=" ")
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        print("")
        children = newchildren


BLACK = 0
RED = 1


class RBNode:
    def __init__(self, key, value):
        self.left  = None
        self.right = None
        self.color = BLACK  # pola parent nie ma -- nie jest w tym zadaniu potrzebne
        self.key   = key
        self.value = value
        # WOLNO dopisac swoje pola


def visit(head, count, ref):
    while head.left is not None or head.right is not None:
        if head.color == BLACK:
            count += 1
        else:
            if (head.left is not None and head.left.color != BLACK) or \
                    (head.right is not None and head.right.color != BLACK):
                return False
        if visit(head.left, count) is False or visit(head.right, count) is False:
            return False
    else:
        if ref is None:
            ref = count
        elif count != ref:
            return False
    return True


def checkRB(T):
    if T.color == RED:
        return False
    ref = None

    def visit(head, count):
        nonlocal ref
        while head.left is not None or head.right is not None:
            if head.color == BLACK:
                count += 1
            else:
                if (head.left is not None and head.left.color != BLACK) or \
                        (head.right is not None and head.right.color != BLACK):
                    return False
            if visit(head.left, count) is False or visit(head.right, count) is False:
                return False
        else:
            if ref is None:
                ref = count
            elif count != ref:
                return False
        return True

    return visit(T, 1)


class BNode:
    def __init__( self, value ):
        self.left   = None
        self.right  = None
        self.parent = None
        self.value  = value


def sumuj(root):
    if root is None:
        return 0
    return root.val + sumuj(root.left) + sumuj(root.right)


tree = BSTDict()
tree.insert(10, "abc")
tree.insert(20, "abc")
tree.insert(5, "abc")
tree.insert(4, "abc")
tree.insert(7, "abc")
tree.insert(6, "abc")
tree.insert(8, "abc")
tree.insert(7.5, "abc")
printChildrenFirst(tree.tree)
tree.remove(10)
tree.remove(20)
printChildrenFirst(tree.tree)




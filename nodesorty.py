class Node:
    def __init__(self):
        self.val = None
        self.next = None


def addBeg(head, node):
    node.next = head
    return node


def addEnd(head, nowy):
    if head is None:
        return nowy
    else:
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = nowy
        return head


def printList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print("")


def length(head):
    res = 0
    while head is not None:
        head = head.next
        res += 1
    return res


def bumbelsort(head):
    n, sort = length(head), False
    for i in range(n):
        prev = None
        temp = head
        for j in range(n-1-i):
            if temp.val > temp.next.val:
                if prev is None:
                    prev = head = temp.next
                else:
                    prev.next = temp.next
                    prev = temp.next
                temp.next.next, temp.next = temp, temp.next.next
                sort = True
            else:
                prev = temp
                temp = temp.next
        if not sort:
            break
    return head


def selectionsort(head):
    n = length(head)
    after = None
    for i in range(n-1):
        miniprev = after
        if after is None:
            mini = prev = head
            cur = head.next
        else:
            mini = prev = after.next
            cur = after.next.next
        while cur is not None:
            if cur.val < mini.val:
                miniprev = prev
                mini = cur
            prev = cur
            cur = cur.next
        if after is None and mini != head:
            miniprev.next = mini.next
            mini.next = head
            head = mini
        elif after is not None and mini != after.next:
            miniprev.next = mini.next
            mini.next = after.next
            after.next = mini
        after = mini
    return head


def insertionsort(head):
    prev = head
    cur = head.next
    while cur is not None:
        tempprev = None
        temp = head
        while cur.val > temp.val and temp != cur:
            tempprev = temp
            temp = temp.next
        if temp != cur:
            prev.next = cur.next
            if tempprev is None:
                cur.next = head
                head = cur
            else:
                cur.next = temp
                tempprev.next = cur
            cur = prev.next
        else:
            prev = cur
            cur = cur.next
    return head



tab = [3, 5, 4, 2, 1]
lista = None
for i in tab:
    nowy = Node()
    nowy.val = i
    lista = addEnd(lista, nowy)

printList(lista)
lista = insertionsort(lista)
printList(lista)


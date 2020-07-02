import random


class Node:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None]*(level+1)  # lista z referencjami do następnych node'ów na poszczególnych poziomach


class SkipList:
    def __init__(self, maxlvl, p):
        self.maxlvl = maxlvl
        self.p = p
        self.header = Node(None, self.maxlvl)
        self.lvl = 0


def search(lista, val):
    current = lista.header
    for i in range(lista.lvl, -1, -1):
        while current.forward[i] is not None and current.forward[i].val < val:
            current = current.forward[i]
    current = current.forward[0]
    if current is not None and current.val == val:
        print("Znaleziono", val)
    else:
        print("Element {} nie wystąpił".format(val))


def insert(lista, val):
    current = lista.header
    update = [None]*(lista.maxlvl+1)

    for i in range(lista.lvl, -1, -1):
        while current.forward[i] is not None and current.forward[i].val < val:
            current = current.forward[i]
        update[i] = current

    current = current.forward[0]
    if current is None or current.val != val:
        level = randomLevel(lista.p, lista.lvl + 1 if lista.lvl < lista.maxlvl else lista.maxlvl)
        if level > lista.lvl:
            update[level] = lista.header
            lista.lvl = level
        new = Node(val, level)
        for i in range(level, -1, -1):
            new.forward[i] = update[i].forward[i]
            update[i].forward[i] = new


def delete(lista, val):
    current = lista.header
    update = [None] * (lista.maxlvl + 1)

    for i in range(lista.lvl, -1, -1):
        while current.forward[i] is not None and current.forward[i].val < val:
            current = current.forward[i]
        update[i] = current

    # usuwanie referencji do elementu
    current = current.forward[0]
    if current is not None and current.val == val:
        for i in range(lista.lvl+1):
            if update[i].forward[i] == current:
                update[i].forward[i] = current.forward[i]

    # usuwanie zbędnych poziomów
    while lista.lvl > 0 and lista.header.forward[lista.lvl] is None:
        lista.lvl -= 1


def randomLevel(p, curlvl):
    lvl = 0
    while random.random() < p and lvl < curlvl:
        lvl += 1
    return lvl


def printList(lista):
    head = lista.header
    for i in range(lista.lvl+1):
        current = head.forward[i]
        print("Level {}: ".format(i), end=" ")
        while current is not None:
            print(current.val, end=" ")
            current = current.forward[i]
        print("")


lista = SkipList(3, 0.5)
insert(lista, 3)
insert(lista, 6)
insert(lista, 7)
insert(lista, 9)
insert(lista, 12)
insert(lista, 19)
insert(lista, 17)
insert(lista, 26)
insert(lista, 21)
insert(lista, 25)
search(lista, 25)
delete(lista, 25)
search(lista, 25)
printList(lista)


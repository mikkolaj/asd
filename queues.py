# implementacja potrzebnych funkcji do kolejki z dwoma końcami
class Node:
    def __init__(self):
        self.next = None
        self.val = None


class Dequeue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def append(self, x):
        new = Node()
        new.val = x
        self.tail.next = new
        self.tail = new

    def appendleft(self, x):
        new = Node()
        new.val = x
        if self.head.next is not None:
            new.next = self.head.next
            self.head.next = new
        else:
            self.head.next = new
            self.tail = new

    def popleft(self):
        item = self.head.next
        self.head.next = self.head.next.next
        if item == self.tail:
            self.tail = self.head
        return item.val

    def is_empty(self):
        if self.head.next is None:
            return True
        return False


class Node:
    def __init__(self):
        self.next = None
        self.val = None


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def put(self, x):
        new = Node()
        new.val = x
        self.tail.next = new
        self.tail = new

    def get(self):
        item = self.head.next
        self.head.next = self.head.next.next
        if item == self.tail:
            self.tail = self.head
        return item.val

    def is_empty(self):
        if self.head.next is None:
            return True
        return False
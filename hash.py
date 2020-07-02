import random
from math import sqrt


def find_prime(x):
    if x % 2 == 0:
        x += 1

    while True:
        prime = True
        for i in range(3, int(sqrt(x)), 2):
            if x % i == 0:
                prime = False
                break
        if prime:
            return x
        x += 2


def universal_hash(key, a, b, p, n):
    return ((a*key + b) % p) % n


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self, n):
        self.size = 2*n
        self.table = [None]*self.size
        self.prime = find_prime(n+1)
        self.a = random.randint(1, self.prime-1)
        self.b = random.randint(0, self.prime-1)

    def add(self, key, val):
        nowy = Node(key, val)
        cur_hash = universal_hash(key, self.a, self.b, self.prime, self.size)
        if self.table[cur_hash] is None:
            self.table[cur_hash] = nowy
        else:
            nowy.next = self.table[cur_hash]
            self.table[cur_hash] = nowy

    def find(self, key):
        cur_hash = universal_hash(key, self.a, self.b, self.prime, self.size)
        cur = self.table[cur_hash]
        while cur is not None:
            if cur.key == key:
                return cur.val
            else:
                cur = cur.next
        return None

    def delete(self, key):
        cur_hash = universal_hash(key, self.a, self.b, self.prime, self.size)
        cur = self.table[cur_hash]
        if cur is not None:
            if cur.key == key:
                self.table[cur_hash] = cur.next
            while cur.next is not None and cur.next.key != key:
                cur = cur.next
            if cur.next is not None and cur.next.key == key:
                cur.next = cur.next.next


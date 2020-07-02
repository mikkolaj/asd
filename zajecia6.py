class Lekcja:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Dana jest lista zajęć opisanych jako czas startu i końca, wybierz największy podzbiór zajęć bez kolizji
# Sortujemy po końcach i wybieramy najwcześniej kończące się zajęcia
def zajecia(lista: Lekcja):
    lista.sort(key=lambda lekcja: lekcja.end)
    wyn = [lista[0]]
    m = 1
    while m < len(lista):
        while lista[m].start < wyn[len(wyn)-1].end:
            m += 1
        wyn.append(lista[m])
        m += 1
    return wyn


def heapifyMin(tab, root):
    largest = root
    left = 2*root+1
    right = 2*root+2

    if left < len(tab) and tab[left] < tab[largest]:
        largest = left

    if right < len(tab) and tab[right] < tab[largest]:
        largest = right

    if largest != root:
        tab[root], tab[largest] = tab[largest], tab[root]
        heapifyMin(tab, largest)


def buildheap(tab):
    for i in range(len(tab)//2, -1, -1):
        heapifyMin(tab, i)


# Dana jest tablica A z ilością wystąpień różnych symboli w tekście, obliczyć ile znaków zająłby tekst zakodowany
# optymalnym kodem Huffmana. Tworzymy MinHeap i łączymy dwa najrzadsze elementy w jeden sumująć do wyniku ich sumaryczną
# ilość wystąpień
def huffman_len(A):
    buildheap(A)
    res = 0
    while len(A) > 1:  # dopóki w kopcu jest więcej niż jeden element, do sumy dodajemy 2 najmniejsze elementy
        mini, A[0] = A[0], A[len(A)-1]  # zabieramy minimalny element z kopca
        A.pop()
        heapifyMin(A, 0)  # znajdujemy drugi minimalny element
        A[0] += mini  # teraz w A[0] będzie suma dwóch minimalnych
        res += A[0]
        heapifyMin(A, 0)
    return res


# Uzyskaj maksymalną wartość zabranych płynów (nie trzeba brać całego płynu)
# Bierzemy po kolei od najwartościowszych płynów, aż do zapełnienia pojemności
def continuousKnapsack(W, P, K):
    A = [(W[i], P[i]/W[i]) for i in range(len(W))]
    A = sorted(A, key=lambda tup: tup[1], reverse=True)
    sum = 0
    for i in A:
        if K > i[0]:
            sum += i[0]*i[1]
            K -= i[0]
        else:
            return sum + K*i[1]
    return sum


# Przejedź trasę z najlepszym kosztem tankowania: jeśli aktualna stacja jest najtańsza - tankuj do pełna,
# jeśli w naszym zasięgu jest stacja, na której jest taniej zatankuj tylko tyle, żeby do niej dojechać
# A - odległości do kolejnych stacji benzynowych i ceny na nich
def minrefuels(A, maxfuel, end):
    pos = 0  # index
    cur = A[0]
    trasa = []
    while True:
        trasa.append(cur)
        if pos + 1 >= len(A):
            if end - cur[0] <= maxfuel:
                return trasa
            else:
                return None

        pos = pos + 1
        best = A[pos]
        if best[0] - cur[0] > maxfuel:  # nie da się dojechać
            return None

        i = pos + 1
        while i < len(A) and A[i][0] <= maxfuel + cur[0]:
            if A[i][1] < best[1]:
                best = A[i]
                pos = i
            i += 1

        if cur[1] < best[1] and end - cur[0] <= maxfuel:
            return trasa
        cur = best


def tasks(A: list):
    A.sort(key=lambda tup: tup[0])
    Cbusy = (False, 0)
    Jbusy = (False, 0)
    res = ""
    for i in A:
        if not Cbusy[0] or Cbusy[1] <= i[0]:
            res += "C"
            Cbusy = (True, i[1])
        elif not Jbusy or Jbusy[1] <= i[0]:
            res += "J"
            Jbusy = (True, i[1])
        else:
            return "IMPOSSIBLE"
    return res



class Kueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def get(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


def width(S, word: str):
    F = [0]*len(word)
    for i in range(len(F)):
        for s in S:
            substr = word[max(0, i-len(s)+1):i+1]
            print(s, substr)
            if s == substr:
                if i - len(s) >= 0:
                    F[i] = max(F[i], min(len(s), F[i-len(s)]))
                else:
                    F[i] = max(F[i], len(s))
    print(F)
    return F[-1]


# P = [7, 2, 5, 10, 8]
# W = [3, 1, 6, 3, 6]
# print(continuousKnapsack(W, P, 7))
test = [(0, 2), (4, 5), (8, 7), (10, 1)]
print(minrefuels(test, 10, 21))

# b = Kueue()
# for i in range(5):
#     b.push(i)
# for i in range(5):
#     print(b.get())

# print(tasks([(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]))
print(width(["ab", "abab", "ba", "bab", "b"], "ababbab"))



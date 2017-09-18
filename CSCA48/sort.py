def bubble_sort(L):
    i = 0
    has_changed = '1' * (len(L)-1)
    while i < len(L) and '1' in has_changed[-len(L)+1:]:
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                has_changed += '1'
            else:
                has_changed += '0'
        i += 1


def selection_sort(L):
    for i in range(len(L)):
        small_index = i
        for j in range(i+1, len(L)):
            if L[j] < L[small_index]:
                small_index = j
        L[i], L[small_index] = L[small_index], L[i]


def quick_sort(L):
    L[:] = quick_sort_helper(L)


def quick_sort_helper(L):
    if len(L) <= 1:
        return L
    pivot = L[-1]
    partition = 0
    for i in range(len(L)-1):
        if L[i] <= pivot:
            L[i], L[partition] = L[partition], L[i]
            partition += 1
    L[-1], L[partition] = L[partition], L[-1]
    return quick_sort_helper(L[:partition]) + quick_sort_helper(L[partition:])


class Heap:

    def __init__(self):
        self._constents = []

    def insert(self, num):
        index = len(self._constents)
        self._constents.append(num)
        parent = (index-1) // 2
        while self._constents[index] < self._constents[parent]:
            self._constents[index], self._constents[parent] =\
                self._constents[parent], self._constents[index]
            index = parent
            parent = (index-1) // 2

    def extract(self):
        num = self._constents.pop(0)
        if self.is_empty():
            return num
        self._constents.insert(0, self._constents.pop())
        index = 0
        left = 2 * index + 1
        right = 2 * index + 2
        while left < len(self._constents) and self._constents[index] >\
              self._constents[left] or right < len(self._constents) and\
              self._constents[index] > self._constents[right]:
            if left < len(self._constents) and right < len(self._constents)\
               and self._constents[index] > self._constents[left] and\
               self._constents[index] > self._constents[right]:
                if left < len(self._constents) and\
                   self._constents[left] < self._constents[right]:
                    self._constents[index], self._constents[left] =\
                        self._constents[left], self._constents[index]
                    index = left
                    left = 2 * index + 1
                    right = 2 * index + 2
                elif right < len(self._constents):
                    self._constents[index], self._constents[right] =\
                        self._constents[right], self._constents[index]
                    index = right
                    left = 2 * index + 1
                    right = 2 * index + 2
            elif left < len(self._constents) and\
                 self._constents[index] > self._constents[left]:
                self._constents[index], self._constents[left] =\
                    self._constents[left], self._constents[index]
                index = left
                left = 2 * index + 1
                right = 2 * index + 2
            elif right < len(self._constents):
                self._constents[index], self._constents[right] =\
                    self._constents[right], self._constents[index]
                index = right
                left = 2 * index + 1
                right = 2 * index + 2
            else:
                left = right = len(self.constents) + 1
        return num

    def is_empty(self):
        return len(self._constents) == 0


def heap_sort(L):
    heap = Heap()
    while L != []:
        heap.insert(L.pop(0))
    while not heap.is_empty():
        L.append(heap.extract())


def merge_sort(L):
    L[:] = merge_sort_helper(L)


def merge_sort_helper(L):
    if len(L) == 1:
        return L
    mid = len(L) // 2
    l1 = merge_sort_helper(L[:mid])
    l2 = merge_sort_helper(L[mid:])
    length = len(l1) + len(l2)
    result = []
    while len(result) < length:
        if l1 == []:
            result = result + l2
        elif l2 == []:
            result = result + l1
        elif l1[0] > l2[0]:
            result.append(l2.pop(0))
        else:
            result.append(l1.pop(0))
    return result

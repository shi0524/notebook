# -*- coding: utf-8 –*-

class MyHeap(object):
    def __init__(self, limit):
        super(MyHeap, self).__init__()
        self.limit = limit
        self.size = 0
        self.heap = [0] * limit

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.limit

    def push(self, value):
        if self.isFull():
            raise RuntimeError("heap is full !!!")

        self.heap[self.size] = value
        self.heap_insert(self.heap, self.size)
        self.size += 1

    def pop(self):
        ans = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heapify(self.heap, 0, self.size)
        return ans

    @classmethod
    def heap_insert(cls, heap, idx):
        up = (idx - 1) / 2
        while up >= 0 and heap[idx] > heap[up]:
            heap[idx], heap[up] = heap[up], heap[idx]
            idx = up
            up = (idx - 1) / 2

    @classmethod
    def heapify(cls, heap, idx, size):
        left = idx * 2 + 1
        while left < size:
            largest = left + 1 if left + 1 < size and heap[left + 1] > heap[left] else left
            largest = largest if heap[largest] > heap[idx] else idx
            if largest == idx:
                break
            heap[largest], heap[idx] = heap[idx], heap[largest]
            idx = largest
            left = idx * 2 + 1


def heapSort(lst):
    if len(lst) < 2:
        return
    size = len(lst)
    for i in range(size - 1, -1, -1):
        MyHeap.heapify(lst, i, size)

    while (size != 0):
        size -= 1
        lst[0], lst[size] = lst[size], lst[0]
        MyHeap.heapify(lst, 0, size)



if __name__ == "__main__":

    lst = [1, 3, 9, 2, 5, 10]
    my_heap = MyHeap(len(lst))
    for i in lst:
        my_heap.push(i)
    sort_list = []
    while not my_heap.isEmpty():
        sort_list.append(my_heap.pop())
    print sort_list

    heapSort(lst)
    print lst


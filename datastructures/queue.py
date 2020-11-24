from datastructures.dynamic_array import DynamicArray
from datastructures.node import LinkedListNode


class LinkedListQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enque(self, val):
        node = LinkedListNode(val, None)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def deque(self):

        if self.head.next is None:
            pop = self.head.val
            self.head, self.tail = None, None
            return pop

        prev, curr = None, self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        pop = curr.val
        prev.next = None
        self.tail = prev
        return pop


class ArrayQueue1:
    """
    Space and time efficient but fixed size (circular)
    """

    def __init__(self, size):

        self.arr = DynamicArray(size)
        self.front, self.back = 0, 0
        self.size = size
        self.remaining_capacity = size

    def enque(self, val):

        if self.remaining_capacity == 0:
            raise ValueError

        self.arr[self.back] = val
        self.back = self.back + 1 % self.size
        self.remaining_capacity -= 1

    def deque(self):
        if self.size == self.remaining_capacity:
            raise ValueError

        pop = self.arr[self.front]
        self.front = self.front + 1 % self.size
        self.back = self.back + 1 % self.size
        self.remaining_capacity += 1
        return pop


class ArrayQueue2:
    """
    Time inefficient
    """

    def __init__(self):

        self.queue = DynamicArray()

    def enque(self, val):

        self.queue.insert(None)
        for idx in range(len(self.queue)-1, 0, -1):
            self.queue[idx] = self.queue[idx-1]
        self.queue[0] = val

    def deque(self):
        return self.queue.pop()


class ArrayQueue3:
    """
    Space inefficient
    """

    def __init__(self):

        self.queue = DynamicArray()
        self.front = 0

    def enque(self, val):

        self.queue.insert(val)

    def deque(self):
        pop = self.queue[self.front]
        self.front += 1
        return pop

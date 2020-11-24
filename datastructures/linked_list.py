from datastructures.dynamic_array import DynamicArray
from datastructures.node import LinkedListNode


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        out = ''

        node = self.head
        while node is not None:
            out += '{} '.format(node.val)
            node = node.next

        return out

    def add_first(self, val):
        node = LinkedListNode(None, val)

        if self.size == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def add_last(self, val):
        node = LinkedListNode(None, val)

        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def delete_first(self,):

        if self.size == 0:
            raise ValueError()
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1

    def delete_last(self):
        self.size -= 1

        if self.size == 0:
            raise ValueError()
        if self.size == 1:
            self.head = self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = None

    def index_of(self, val):
        counter = 0

        node = self.head
        while node is not None:
            if node.val == val:
                return counter
            counter += 1
            node = node.next

        return -1

    def contains(self, val):
        return self.index_of(val) != -1

    def to_array(self):
        if self.size == 0:
            raise ValueError

        arr = DynamicArray()
        curr = self.head
        while curr is not None:
            arr.insert(curr.val)
            curr = curr.next

        return arr

    def reverse(self):

        if self.size == 0:
            raise ValueError
        elif self.size == 1:
            return
        else:
            prev, curr = None, self.head
            while curr is not None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            self.head, self.tail = self.tail, self.head

    def kth_node(self, k):

        slow, fast = self.head, self.head

        while fast.next is not None:
            fast = fast.next

            if k > 0:
                k -= 1
            else:
                slow = slow.next

        return slow

    def middle(self):

        if self.head.next is None:
            return self.head.next

        slow, fast = self.head, self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        if fast is None:
            return prev_slow, slow
        else:
            return slow

    @staticmethod
    def make_cycle(head):
        fast, slow = head, head
        fast = fast.next.next
        slow = slow.next
        fast.next = slow

    @staticmethod
    def floyds_cycle_finding_algorithm(head):

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False


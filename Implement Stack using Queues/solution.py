class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def to_add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    def to_pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item.item
        raise ValueError('Queue is empty.')
    @property
    def to_peek(self):
        return self.head

class MyStack:
    def __init__(self):
        self.sth = Queue()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        reversed_queue = Queue()
        while not self.sth.is_empty():
            reversed_queue.to_add(self.sth.to_pop())
        reversed_queue.to_add(x)
        while not reversed_queue.is_empty():
            self.sth.to_add(reversed_queue.to_pop())
    def pop(self):
        """
        :rtype: int
        """
        item = self.sth.to_pop()
        return item
    def top(self):
        """
        :rtype: int
        """
        item = self.sth.to_peek
        return item
    def empty(self):
        """
        :rtype: bool
        """
        return self.sth.is_empty()

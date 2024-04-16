class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def to_push(self, item):
        self.head = Node(item, self.head)
    def to_pop(self):
        item = self.head.item
        self.head = self.head.next
        return item
    @property
    def to_peek(self):
        if self.head:
            return self.head.item
        raise ValueError('Stack is empty')
class MyQueue(Stack):
    def __init__(self):
        super().__init__()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        reversed_stack = Stack()
        while not self.is_empty():
            reversed_stack.to_push(self.to_pop())
        reversed_stack.to_push(x)
        while not reversed_stack.is_empty():
            self.to_push(reversed_stack.to_pop())
    def pop(self):
        """
        :rtype: int
        """
        item = self.to_pop()
        return item
    def peek(self):
        """
        :rtype: int
        """
        item = self.to_peek
        return item
    def empty(self):
        """
        :rtype: bool
        """
        return self.is_empty()

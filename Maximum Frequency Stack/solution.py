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
class FreqStack:
    def __init__(self):
        self.head = None
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.head = Node(val, self.head)
    def pop(self):
        """
        :rtype: int
        """
        def dict_(stack, val):
            """Works similiarly to a dictionary"""
            current = stack.head
            while current is not None:
                if current.item.item == val:
                    current.item.next += 1
                    return
                if current.next is None:
                    current.next = Node(Node(val, 1), None)
                    return
                current = current.next
            stack.head = Node(Node(val, 1), None)
        current = self.head
        new_stack = Stack()
        while current is not None:
            dict_(new_stack, current.item)
            current = current.next
        new_current = new_stack.head
        max_value, max_count = 0, 0
        while new_current is not None:
            if new_current.item.next > max_count:
                max_count = new_current.item.next
                max_value = new_current.item.item
            new_current = new_current.next
        current_behind = None
        current_ahead = self.head
        while current_ahead is not None:
            if current_ahead.item == max_value:
                if current_behind is None:
                    self.head = current_ahead.next
                    current_behind = current_ahead.next
                    if current_behind is None:
                        current_ahead = None
                    else:
                        current_ahead = current_behind.next
                else:
                    current_behind.next = current_ahead.next
                    current_ahead = current_behind.next
                break
            else:
                current_behind = current_ahead
                current_ahead = current_behind.next
        return max_value

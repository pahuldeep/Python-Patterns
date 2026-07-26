class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, e):
        new = Node(e)
        new.next = self.head
        self.head = new
        if self.size == 0:
            self.tail = new
        self.size += 1

    def add_last(self, e):
        new = Node(e)
        if self.tail:
            self.tail.next = new
        self.tail = new
        if self.size == 0:
            self.head = new
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return 0
        self.head = self.head.next
        self.size -= 1

    def to_array(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

"""
Implement an algorithm to find the kth to last element of a singly linked
list.
"""


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tailval = None
        self.length = 0

    def add_node(self, value):
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        self.length += 1

    def traverseLL(self):
        current = self.head
        ll_length = 0
        while current:
            ll_length += 1
            print(current.dataval)
            current = current.next
        return ll_length

    def find_nth_to_last(self, index):
        current = self.head
        if index < 0 > self.length:
            return False
        for i in range(self.length - index - 1):
            current = current.next
        print(current.dataval)


sll = SLinkedList()

sll.add_node(0)
sll.add_node(1)
sll.add_node(2)
sll.add_node(3)
sll.add_node(4)
sll.add_node(5)
sll.add_node(6)
sll.add_node(7)
sll.find_nth_to_last(1)

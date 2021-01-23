"""
Implement an algorithm to delete a node in the middle (i.e., any node but the
first and the last node, not necesarily the exact middle) of a singly linked
list, given access to that node.
Example:
    Input: the node c from the linked list a->b->c->d->e->f
    Output: nothing is returned, but the new linked list looks like:
        a->b->d->e->f->
"""
import math


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

    def remove_middle(self):
        middle = math.floor(self.length / 2)
        current = self.head
        previous = None
        if self.length < 3:
            return False
        for i in range(self.length):
            if i == middle:
                previous.next = current.next
                break
            else:
                previous = current
                current = previous.next


sll = SLinkedList()

sll.add_node(0)
sll.add_node(1)
sll.add_node(2)
sll.add_node(3)
sll.add_node(4)
sll.add_node(5)
sll.add_node(6)
sll.add_node(7)
sll.remove_middle()
sll.remove_middle()
sll.traverseLL()

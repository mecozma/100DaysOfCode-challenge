"""
Write code to remove duplicates from an unsorted linked list.
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

    # def add_node(self, value):
    #     node = Node(value)
    #     if not self.headval:
    #         self.headval = node
    #         self.tailval = self.headval
    #         print(self.headval.dataval, "if")
    #     else:
    #         self.tailval.next = node
    #         self.tail = node
    #         print(self.tailval.dataval, "tail")
    #     self.length += 1

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
        while current:
            print(current.dataval)
            current = current.next

    def rm_dup(self):
        unique = set()
        current = self.head
        previous = None
        while current:
            if current.dataval in unique:
                previous.next = current.next
                self.length -= 1
            else:
                unique.add(current.dataval)
                previous = current
            current = previous.next
        return self.length


sll = SLinkedList()

sll.add_node(0)
sll.add_node(1)
sll.add_node(3)
sll.add_node(2)
sll.add_node(0)
sll.add_node(2)
sll.add_node(0)
sll.add_node(3)
print("prev length", sll.length)
sll.traverseLL()
sll.rm_dup()
print("current length", sll.length)
sll.traverseLL()

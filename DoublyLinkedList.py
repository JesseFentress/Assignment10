class DoubleNode:

    def __init__(self, data):
        self.data = data
        self.head = None
        self.tail = None

class DoublyLinkedList:


    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
            return "Successful append onto empty doubly linked list"
        else:
            self.last.tail = new_node
            new_node.head = self.last
            self.last = new_node
            return "Successful append onto doubly linked list"

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.tail

    def start_insert(self, data):
        new_node = DoubleNode(data)
        if self.head is not None:
            new_node.tail = self.head
            self.head.head = new_node
            self.head = new_node
            return "Insertion to start of list complete"
        else:
            self.head = new_node
            self.last = new_node
            return "Insertion to start of empty list complete"

    def middle_insert(self, data, node):
        new_node = DoubleNode(data)
        curr = self.head
        while curr is not None:
            if curr.tail.data == node:
                new_node.tail = curr.tail
                curr.tail.head = new_node
                curr.tail = new_node
                new_node.head = curr
                return "Middle insert compelete"
            else:
                curr = curr.tail
        return "Desired node not found"

    def end_insert(self, data):
        new_node = DoubleNode(data)
        if self.head is not None:
            self.last.tail = new_node
            new_node.head = self.last
            self.last = new_node
            return "End insert on empty list complete"
        else:
            self.head = new_node
            self.last = new_node
            return "End insert compelte"

    def delete(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                if curr is self.head:
                    self.head = curr.tail
                    curr.tail = None
                    self.head.head = None
                    return "Deletion of head node complete"
                elif curr is self.last:
                    self.last = curr.head
                    curr.head = None
                    self.last.tail = None
                    return "Deletion of last node complete"
                else:
                    curr.head.tail = curr.tail
                    curr.tail = curr.head
                    curr.head = None
                    curr.tail = None
                    return "Deletion of middle node compelete"
            else:
                curr = curr.tail
        return "Desired node not found"




a = DoublyLinkedList()
n = 5

for i in range(n):
    data = int(input('Enter data: '))
    a.append(data)

a.display()
print()
print(a.start_insert(99))
a.display()
print()
print(a.middle_insert(50, 3))
a.display()
print()
print(a.end_insert(44))
a.display()
print()
print(a.delete(5))
a.display()
print()

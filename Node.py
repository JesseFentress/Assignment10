

class Node:

    def __init__(self, data):
        self.data = data
        self.tail = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.tail = Node(data)
            self.last = self.last.tail

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.tail

    def print_head(self):
        print(self.head.data)

    def start_insert(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.tail = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.last = new_node


    def middle_insert(self, data, node):
        new_node = Node(data)
        curr = self.head
        if self.head is not None:
            while curr is not None:
                if curr.data == node:

                    last = curr
                    curr = curr.tail
                    new_node.tail = curr
                    last.tail = new_node
                    return "Middle insert complete"
                else:
                    curr = curr.tail
        else:
            return "Linked list is empty"



    def end_instert(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.last.tail = new_node
            self.last = new_node
            return "End insert complete"
        else:
            self.head.tail = new_node
            self.last = new_node
            return "End insert on single node linked list complete"

    def delete(self, data):
        del_value = data
        curr = self.head
        while curr is not None:
            if curr.data == del_value:
                if curr is self.head:
                    temp = self.head
                    self.head = self.head.tail
                    temp.tail = None
                    return "Successful deletion of head node"
                elif curr is self.last:
                    prev.tail = None
                    curr.tail = None
                    self.last = prev
                    return "Successful deletion of tail node"
                else:
                    prev.tail = curr.tail
                    curr.tail = None
                    return "Successful deletion of middle node"
            else:
                prev = curr
                curr = curr.tail
        return "Node was not found"



    def traverse(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodess.append(curr.data)
            curr = curr.tail

    def reverse(self):
        curr = self.head
        print_list = []
        while curr is not None:
            print_list.append(curr.data)
            curr = curr.tail
        print("Reversed linked list")
        for node in range(len(print_list)):
            print(print_list.pop(), end=' ')




a = LinkedList()
n = 5

for i in range(n):
    data = int(input('Enter data: '))
    a.append(data)

a.display()
print()
print(a.middle_insert(14, 4))
a.display()
print()
print(a.end_instert(99))
a.display()
print()
print(a.delete(1))
a.display()
print()
a.reverse()
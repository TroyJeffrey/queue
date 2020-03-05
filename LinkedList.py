class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None


    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self, data):
        new_node = Node(data=data)
        if self.head :
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head

    def push_end(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node



# Troy Jeffrey Amegashie
# Queue
# 03/05/2020

from LinkedList import LinkedListTail


class Queue:
    def __init__(self):
        self.myqueue = LinkedListTail()

    def push(self, data):
        self.myqueue.push_end(data)

    def pop(self, data):
        self.myqueue.remove_head()


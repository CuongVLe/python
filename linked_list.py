#linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        if self.tail != None:
            self.tail.next = newNode
        self.tail = newNode

    def removeNode(self, index):
        prev = None
        node = self.head
        i = 0
        while (node != None) and (i < index):
            prev = node
            node = node.next
            i += 1
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next

    def printList(self):
        node = self.head
        while node != None:
            print node.data
            node = node.next
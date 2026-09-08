# ============================================
# A) SINGLY LINKED LIST
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


print("----- A) Singly Linked List -----")

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()


# ============================================
# B) DOUBLY LINKED LIST
# ============================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DoublyNode(data)

        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


print("\n----- B) Doubly Linked List -----")

dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)

dll.display()


# ============================================
# C) CIRCULAR LINKED LIST
# ============================================

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CircularNode(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head

        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def display(self):
        temp = self.head

        if self.head:
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next

                if temp == self.head:
                    break

            print("(back to head)")


print("\n----- C) Circular Linked List -----")

cll = CircularLinkedList()

cll.insert(5)
cll.insert(10)
cll.insert(15)

cll.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_nodes(self):
        curr = self.head
        while curr is not None:
            print(curr.data)

            curr = curr.next

    def print_odd_nodes(self):
        i = 0

        curr = self.head
        while curr is not None:
            if i % 2 != 0:
                print(curr.data)

            curr = curr.next
            i += 1

    def remove(self, node):
        if self.head is node:
            self.head = node.next

            if self.head is None:
                self.tail = None
                return

        curr = self.head
        while curr.next is not None:
            if curr.next is node:
                curr.next = curr.next.next
                break

            curr = curr.next

        if curr.next is None:
            self.tail = curr

    def append(self, node):
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node


class DblNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DblLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node

        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node

        self.tail = node

    def remove(self, node):
        if node.prev is None:
            # If node.prev is None, it means this node is the head of
            # the list. To remove it, just reassign self.head to the next
            # node
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            # If node.next is None, it means this node is the tail of
            # the list. To remove it, reassign self.tail to the previous
            # node
            self.tail = node.prev
        else:
            node.next.prev = node.prev


def has_consecutive(node):
    prev = None
    curr = node
    while curr is not None:
        if curr.data == prev.data:
            return True

        prev = curr
        curr = curr.next

    return False


def remove_value(node, value):
    if node.data == value:
        return node.next

    curr = node
    while curr.next is not None:
        if curr.next.data == value:
            curr.next = curr.next.next
            break

        curr = curr.next

    return node


def reverse_llist(node):
    # Use a stack to store all nodes in the linked list
    stack = []

    curr = node
    while curr is not None:
        stack.append(curr)

        curr = curr.next

    # Nodes will be popped in reverse order due to the nature of stacks.
    reversed_llist = stack.pop()

    curr = reversed_llist
    while len(stack) != 0:
        curr.next = stack.pop()
        curr = curr.next

    return reversed_llist

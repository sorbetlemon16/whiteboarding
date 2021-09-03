"""Solutions for Whiteboarding 5"""


def get_length(lst):
    if not lst:
        return 0

    return 1 + get_length(lst[1:])


def sum_nums(lst):
    if not lst:
        return 0

    return lst[0] + sum_nums(lst[1:])


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        """Add `item` to the queue."""

        self.data.insert(0, item)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head):
    current = head

    while current:
        print(current)

        current = current.next


def print_tree(root):
    nodes = [root]

    while nodes:
        current = nodes.pop()

        print(current.data)

        nodes.extend(current.children)


def merge_sorted(lst1, lst2):
    merged = []

    i = j = 0
    while i < len(lst1) and j < len(lst2):
        num1, num2 = lst1[i], lst2[j]

        if num1 <= num2:
            merged.append(num1)
            i += 1

        if num1 >= num2:
            merged.append(num2)
            j += 1

    if i < len(lst1):
        merged.extend(lst1)
    elif j < len(lst2):
        merged.extend(lst2)

    return merged

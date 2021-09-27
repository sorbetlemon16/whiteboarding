class Node(object):
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def count_nodes_iterative_bfs(self):
        """Return the number of nodes in the tree using iterative
        breadth first traversal.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.count_nodes_iterative_bfs()
        10
        """

        count = 0

        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            count += 1
            for child in current.children:
                to_visit.append(child)

        return count

    def count_nodes_iterative_bfs(self):
        """Return the number of nodes in the tree using iterative
        depth first traversal.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.count_nodes_iterative_bfs()
        10
        """

        count = 0

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()
            count += 1
            to_visit.extend(current.children)

        return count

    def count_nodes_recursive(self):
        """Return the number of nodes in the tree using recursion.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.count_nodes_recursive()
        10
        """

        return 1 + sum([n.count_nodes_recursive() for n in self.children])

    def has_duplicate(self):
        """Return True if tree contains duplicate data.

        This solution traverses depth-first, although you can also traverse
        breadth-first by checking & removing the first item from `to_visit`.
        """

        to_visit = [self]
        data = set()

        while to_visit:
            current = to_visit.pop()

            if current.data in data:
                return True

            data.add(current.data)
            to_visit.extend(current.children)

        return False

    def tree_contains_iterative_bfs(self, item):
        """Return True if any node's data in the tree matches item.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.tree_contains_iterative_bfs("third_gen_4")
        True
        >>> root.tree_contains_iterative_bfs("this is not in the tree")
        False
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            if current.data == item:
                return True
            for child in current.children:
                to_visit.append(child)

        return False

    def tree_contains_iterative_dfs(self, item):
        """Return True if any node's data in the tree matches item.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.tree_contains_iterative_dfs("third_gen_4")
        True
        >>> root.tree_contains_iterative_dfs("this is not in the tree")
        False
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == item:
                return True

            to_visit.extend(current.children)

        return False

    def tree_contains_recursive(self, item):
        """Find the highest ranking matching node in the tree.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.tree_contains_recursive("third_gen_4")
        True
        >>> root.tree_contains_recursive("this is not in the tree")
        False
        """
        if self.data == item:
            return True
        elif self.children:
            return any([n.tree_contains_recursive(item) for n in self.children])
        else:
            return False

    def find_highest_ranking_iterative(self, item):
        """Find the highest ranking matching node in the tree.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> found = root.find_highest_ranking_iterative('duplicate')
        >>> found is second_gen_1
        True
        >>> found is fourth_gen_1
        False
        >>> notfound = root.find_highest_ranking_iterative('not in tree')
        >>> notfound is None
        True
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            if current.data == item:
                return current
            for child in current.children:
                to_visit.append(child)

    def find_lowest_ranking_iterative(self, item):
        """Find the lowest ranking matching node in the tree.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> found = root.find_lowest_ranking_iterative('duplicate')
        >>> found is second_gen_1
        False
        >>> found is fourth_gen_1
        True
        >>> found is None
        False
        >>> notfound = root.find_lowest_ranking_iterative('not in tree')
        >>> notfound is None
        True
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        found = None

        while to_visit:
            current = to_visit.popleft()
            if current.data == item:
                found = current
            for child in current.children:
                to_visit.append(child)

        return found

    def insert_item_iterative(self, item, node):
        """Insert the given node as a child of the first node whose data
        matches item. Return True if successful, False otherwise.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> new_node = Node("I am a new node", [])
        >>> root.insert_item_iterative("duplicate", new_node)
        True
        >>> new_node in second_gen_1.children
        True
        >>> root.insert_item_iterative("not in tree", new_node)
        False
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            if current.data == item:
                current.children.append(node)
                return True
            for child in current.children:
                to_visit.append(child)

        return False

    def remove_nodes_destructive_iterative(self, item):
        """Insert the given node as a child of the first node whose data
        matches item. Return True if successful, False otherwise.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.remove_nodes_destructive_iterative('duplicate')
        >>> fourth_gen_1 in third_gen_2.children
        False
        >>> second_gen_1 in root.children
        False
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            for child in current.children:
                if child.data == item:
                    current.children.remove(child)
            for child in current.children:
                to_visit.append(child)

    def remove_nodes_non_destructive_iterative(self, item):
        """Insert the given node as a child of the first node whose data
        matches item. Return True if successful, False otherwise.

        >>> fourth_gen_1 = Node("duplicate", [])
        >>> fourth_gen_2 = Node("fourth_gen_2", [])
        >>> fourth_gen_3 = Node("fourth_gen_3", [])
        >>> third_gen_1 = Node("third_gen_1", [])
        >>> third_gen_2 = Node("third_gen_2", [fourth_gen_1, fourth_gen_2])
        >>> third_gen_3 = Node("third_gen_3", [])
        >>> third_gen_4 = Node("third_gen_4", [fourth_gen_3])
        >>> second_gen_1 = Node("duplicate", [third_gen_1])
        >>> second_gen_2 = Node("second_gen_2", [third_gen_2, third_gen_3, third_gen_4])
        >>> root = Node('root', [second_gen_1, second_gen_2])
        >>> root.remove_nodes_non_destructive_iterative('duplicate')
        >>> fourth_gen_1 in third_gen_2.children
        False
        >>> second_gen_1 in root.children
        False
        >>> third_gen_1 in root.children
        True
        """
        from collections import deque

        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            for child in current.children:
                if child.data == item:
                    current.children.remove(child)
                    current.children.extend(child.children)
            for child in current.children:
                to_visit.append(child)

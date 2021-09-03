class Node:
    """A graph node."""

    def __init__(self, data, adjacent=None):
        self.data = data
        self.adjacent = adjacent or set()

    def __repr__(self):
        return f'<Node {self.data}>'


class Graph:
    """A graph."""

    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        self.nodes.add(node)

    def connect_nodes(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)


def print_nodes(node):
    seen = set([node])
    to_visit = [node]

    while to_visit:
        current = to_visit.pop()
        print(current)

        for node in current.adjacent - seen:
            to_visit.append(node)
            seen.add(node)


def print_nodes_recursively(node, seen=None):
    print(node)

    seen = seen or set()
    seen.add(node)

    for nd in node.adjacent:
        if nd not in seen:
            print_nodes_recursively(nd, seen)


def has_connection(node1, node2):
    seen = set([node1])
    to_visit = [node1]

    while to_visit:
        current = to_visit.pop()
        if current is node2:
            return True
        else:
            for node in current.adjacent - seen:
                to_visit.append(node)
                seen.add(node)

    return False


def has_connection_recursive(node1, node2, seen=None):
    if node1 is node2:
        return True

    seen = seen or set()
    seen.add(node1)

    for node in node1.adjacent:
        if node not in seen:
            if has_connection_recursive(node, node2, seen):
                return True

    return False


def get_edges(node):
    seen = set()
    to_visit = [node]
    edges = []

    while to_visit:
        parent_node = to_visit.pop()

        if parent_node not in seen:
            seen.add(parent_node)

            for node in parent_node.adjacent:
                edges.append((parent_node, node))
                to_visit.append(node)
    return edges


def find_all_paths(start, end, path=None):
    path = path or []
    path = path + [start]

    if start is end:
        return [path]

    all_paths = []
    for node in start.adjacent:
        if node not in set(path):
            paths = find_all_paths(node, end, path)
            all_paths.extend(paths)

    return all_paths

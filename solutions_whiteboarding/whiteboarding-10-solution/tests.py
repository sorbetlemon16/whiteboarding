import unittest
from whiteboarding_10 import (Graph, Node, has_connection,
                              has_connection_recursive, get_edges)


class GraphSetup(unittest.TestCase):
    def setUp(self):
        self.simple_graph = Graph()
        a, b, c = Node('A'), Node('B'), Node('C')
        self.simple_graph.connect_nodes(a, b)
        self.simple_graph.connect_nodes(a, c)
        self.simple_graph.connect_nodes(b, c)
        self.simple_graph.node_table = {'A': a,
                                        'B': b,
                                        'C': c}

        self.disconnected_graph = Graph()
        a, b, c, d, e = Node('A'), Node('B'), Node('C'), Node('D'), Node('E')
        self.disconnected_graph.connect_nodes(a, b)
        self.disconnected_graph.connect_nodes(a, c)
        self.disconnected_graph.connect_nodes(a, d)
        self.disconnected_graph.connect_nodes(b, c)
        self.disconnected_graph.add_node(e)
        self.disconnected_graph.node_table = {'A': a,
                                              'B': b,
                                              'C': c,
                                              'D': d,
                                              'E': e}

        self.larger_graph = Graph()
        a, b, c, d, e, f = [Node('A'), Node('B'), Node('C'),
                            Node('D'), Node('E'), Node('F'), ]
        self.larger_graph.connect_nodes(a, b)
        self.larger_graph.connect_nodes(a, d)
        self.larger_graph.connect_nodes(b, c)
        self.larger_graph.connect_nodes(b, e)
        self.larger_graph.connect_nodes(c, a)
        self.larger_graph.connect_nodes(a, d)
        self.larger_graph.connect_nodes(d, e)
        self.larger_graph.connect_nodes(e, f)
        self.larger_graph.add_node(e)
        self.larger_graph.node_table = {'A': a,
                                        'B': b,
                                        'C': c,
                                        'D': d,
                                        'E': e,
                                        'F': f}


class TestMediumChallenges(GraphSetup):
    def test_has_connection(self):
        result = has_connection(self.simple_graph.node_table['A'],
                                self.simple_graph.node_table['C'])
        self.assertIs(result, True)

        result = has_connection(self.disconnected_graph.node_table['A'],
                                self.disconnected_graph.node_table['E'])
        self.assertIs(result, False)

    def test_has_connection_recursive(self):
        simple, disconnected = self.simple_graph, self.disconnected_graph

        result = has_connection_recursive(simple.node_table['A'],
                                          simple.node_table['C'])
        self.assertIs(result, True)

        result = has_connection_recursive(disconnected.node_table['A'],
                                          disconnected.node_table['E'])
        self.assertIs(result, False)

    def test_get_edges(self):
        a, b, c = self.simple_graph.node_table.values()

        result = get_edges(self.simple_graph.node_table['A'])
        correct_result = [(a, b), (a, c), (b, c), (b, a), (c, a), (c, b)]

        self.assertEquals(set(result), set(correct_result))


if __name__ == '__main__':
    unittest.main(verbosity=2)

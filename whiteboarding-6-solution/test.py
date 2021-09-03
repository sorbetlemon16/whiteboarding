import unittest
from unittest.mock import patch
import io
from whiteboarding_6 import (Node, LinkedList, DblNode, DblLinkedList,
                             remove_value, reverse_llist)


class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        a, b, c = Node("a"), Node("b"), Node("c")
        a.next, b.next = b, c

        self.a_node, self.b_node, self.c_node = a, b, c

        self.llist = LinkedList()
        self.llist.head = a
        self.llist.tail = c

    def test_print_nodes(self):
        """Test print_nodes should print each item in list."""

        with patch("sys.stdout", new_callable=io.StringIO) as output:
            self.llist.print_nodes()

        self.assertEqual(output.getvalue(), "a\nb\nc\n")

    def test_print_odd_nodes(self):
        """Test print_odd_nodes should print odd numbered nodes."""

        with patch("sys.stdout", new_callable=io.StringIO) as output:
            self.llist.print_odd_nodes()

        self.assertEqual(output.getvalue(), "b\n")

    def test_remove_head(self):
        self.llist.remove(self.llist.head)

        self.assertEqual(self.llist.head, self.b_node)
        self.assertEqual(self.llist.tail, self.c_node)

    def test_remove_middle(self):
        self.llist.remove(self.b_node)

        self.assertEqual(self.llist.head.data, "a")
        self.assertEqual(self.llist.tail.data, "c")

    def test_remove_tail(self):
        self.llist.remove(self.llist.tail)

        self.assertEqual(self.llist.head.data, "a")
        self.assertEqual(self.llist.tail.data, "b")

    def test_remove_all(self):
        self.llist.remove(self.a_node)
        self.llist.remove(self.b_node)
        self.llist.remove(self.c_node)

        self.assertIsNone(self.llist.head)
        self.assertIsNone(self.llist.tail)

    def test_append(self):
        llist = LinkedList()

        llist.append(Node(1))
        llist.append(Node(2))
        llist.append(Node(3))

        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.head.next.data, 2)
        self.assertEqual(llist.head.next.next.data, 3)
        self.assertEqual(llist.tail.data, 3)

    def test_remove_value(self):
        node = remove_value(self.a_node, "b")

        self.assertEqual(node.data, "a")
        self.assertEqual(node.next.data, "c")
        self.assertIsNone(node.next.next)

    def test_remove_value2(self):
        node = remove_value(self.a_node, "a")

        self.assertEqual(node.data, "b")

    def test_reverse_llist(self):
        rev_node = reverse_llist(self.a_node)

        self.assertEqual(rev_node, self.c_node)
        self.assertEqual(rev_node.next, self.b_node)
        self.assertEqual(rev_node.next.next, self.a_node)



if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch
from unittest import TestCase
from io import StringIO
from solution import (print_each, print_first_and_word, print_every_other,
                      find_item, get_length, print_len_words, get_max)


class TestSolution(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_each(self, out):
        print_each([1, 2])
        self.assertEqual(out.getvalue(), '1\n2\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_first_and_word(self, out):
        print_first_and_word(['hi'])
        self.assertEqual(out.getvalue(), "('h', 'hi')\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_every_other(self, out):
        print_every_other([1, 2, 3])
        self.assertEqual(out.getvalue(), '1\n3\n')

    def test_find_item(self):
        self.assertEqual(find_item([1], 1), True)
        self.assertEqual(find_item([], 1), False)

    def test_get_length(self):
        self.assertEqual(get_length('123'), 3)
        self.assertEqual(get_length(''), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_len_words(self, out):
        print_len_words('a aa')
        self.assertEqual(out.getvalue(), '1\n2\n')

    def get_max(self):
        self.assertEqual(get_max([0, 0, 2]), 2)
        self.assertEqual(get_max([0]), 0)
        self.assertEqual(get_max([]), None)


if __name__ == '__main__':
    unittest.main()

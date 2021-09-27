"""Unittests for Whiteboarding 2 Solutions"""


import unittest
from unittest import TestCase
from solution import (get_longest, get_item_count, get_even_num_idx,
                      replace_vowels, get_unique_chars, get_char_count,
                      is_anagram)


class TestSolution(TestCase):
    def test_get_longest(self):
        self.assertEqual(get_longest(['a', 'aa', 'aba']), 'aba')

    def test_get_item_count(self):
        self.assertEqual(get_item_count([1, 1, 0], 1), 2)
        self.assertEqual(get_item_count([0], 1), 0)

    def test_get_even_num_idx(self):
        self.assertEqual(get_even_num_idx([2, 4, 1]), [0, 1])
        self.assertEqual(get_even_num_idx([1]), [])

    def test_replace_vowels(self):
        self.assertEqual(replace_vowels('hello'), 'h*ll*')

    def test_get_unique_chars(self):
        self.assertEqual(get_unique_chars('aaba'), ['a', 'b'])

    def test_get_char_count(self):
        self.assertEqual(get_char_count('cat'), {'c': 1,
                                                 'a': 1,
                                                 't': 1})

    def test_is_anagram(self):
        self.assertEqual(is_anagram('moon', 'noom'), True)
        self.assertEqual(is_anagram('bat', 'a'), False)


if __name__ == '__main__':
    unittest.main()

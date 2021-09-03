"""Whiteboarding 2 Solutions"""


def get_longest(strings):
    longest = strings[0]

    for s in strings:
        if len(s) > len(longest):
            longest = s

    return s


def get_item_count(items, item):
    count = 0

    for el in items:
        if el == item:
            count += 1

    return count


def get_even_num_idx(nums):
    return [i for i, n in enumerate(nums) if n % 2 == 0]


def replace_vowels(string):
    vowels = set('aeiou')

    return ''.join(['*' if char in vowels else char for char in string])


def get_unique_chars(string):
    return list(set(string))


def get_char_count(string):
    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    return counts


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

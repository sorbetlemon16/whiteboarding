"""Whiteboarding 3 Solutions"""


def largest_smaller(nums, n):
    result = None

    for num in nums:
        if num < n:
            if not result or result < num:
                result = num

    return result


def add_to_zero(nums):
    nums_set = set(nums)

    for n in nums:
        if -n in nums_set:
            return True

    return False


def is_pangram(s):
    letters = set()

    lowercased = s.lower()
    for c in lowercased:
        if c.isalpha():
            letters.add(c)

    return len(letters) == 26


def reverse_digits(n):
    rev_digits = reversed(str(n))

    return int("".join(rev_digits))


def truncate_chars(s):
    curr_char = s[0]
    result = [s[0]]

    for c in s:
        if c != curr_char:
            result.append(c)
            curr_char = c

    return "".join(s)

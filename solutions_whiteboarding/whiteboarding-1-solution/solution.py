"""Whiteboarding 1 Solutions"""


def print_each(lst):
    for item in lst:
        print(item)


def print_first_and_word(words):
    for word in words:
        print((word[0], word))


def print_every_other(nums):
    for num in nums[::2]:
        print(num)


def find_item(lst, item):
    return item in set(lst)


def get_length(str):
    length = 0
    for char in str:
        length += 1

    return length


def print_len_words(sentence):
    for word in sentence.split():
        print(len(word))


def get_max(nums):
    if not nums:
        return

    max_n = nums[0]

    for num in nums:
        if num > max_n:
            max_n = num

    return max_n

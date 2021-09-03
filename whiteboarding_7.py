def print_list(lst):
    if len(lst) == 0:
        return

    print(lst[0])

    print_list(lst[1:])


def print_nums(n=1):
    if n > 5:
        return

    print(n)

    print_nums(n + 1)


def max_num(nums, max_n=None):
    if max_n is None and len(nums) > 0:
        max_n = nums[0]

    if len(nums) <= 1:
        return max_n

    n = nums.pop()
    if n > max_n:
        max_n = n

    return max_num(nums, max_n)


def double_nums(nums, i=0):
    if len(nums) == 0:
        return None

    if i >= len(nums):
        return nums

    nums[i] = nums[i] * 2

    return double_nums(nums, i + 1)


def reverse_str(s):
    if len(s) <= 1:
        return s[0]

    return reverse_str(s[1:]) + reverse_str(s[0])


def flatten(lst, result=None):
    result = result or []

    for el in lst:
        if type(el) is list:
            flatten(el, result)
        else:
            result.append(el)

    return result

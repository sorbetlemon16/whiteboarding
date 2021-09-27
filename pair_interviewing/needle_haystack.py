def recursive_index(needle, haystack, index=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # START SOLUTION

    # Check if we've reached the end of the list and it was not found
    if index == len(haystack):
        return None

    # Have we found it?
    if haystack[index] == needle:
        return index

    return recursive_index(needle, haystack, index + 1)

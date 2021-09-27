"""Whiteboarding 4 Solutions"""


def snake_to_camel(snakecase):
    tokens = snakecase.split("_")
    result = [tokens[0]]

    for token in tokens[1:]:
        result.append(token.title())

    return "".join(result)


def validate_passcode(required_char, char_min, char_max, passcode):
    req_chars = []
    for char in passcode:
        if char == required_char:
            req_chars.append(char)

    return char_min <= len(req_chars) <= char_max


def reverse_list(lst):
    for i in range(len(lst) // 2):
        # `opposite_i` is the index number of the element on the opposite
        # side of the list. For example, the oppsite of index 0 is
        # index -1.
        opposite_i = -i - 1

        lst[i], lst[opposite_i] = lst[opposite_i], lst[i]


def group_anagrams(words):
    anagrams = {}
    for word in words:
        hashed_word = "".join(sorted(word))

        if hashed_word not in anagrams:
            anagrams[hashed_word] = [word]
        else:
            anagrams[hashed_word].append(word)

    return list(anagrams.values())

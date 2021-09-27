def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    # START SOLUTION

    lowercase_vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0

    for letter in word:

        if letter.lower() in lowercase_vowels:
            vowel_count = vowel_count + 1

    return vowel_count > (len(word) / 2)
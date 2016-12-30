def count_recursively(lst):
    """ Count list using recursion

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


def binary_search(val):
    """ Guess for a val from 1 to 100

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """
    # 1 to 100
    # 1 to 50, 51 to 100
    # 1 to 25, 26 to 50, 51 to 75, 76 to 100
    low = 0
    high = 101
    guess = None
    tries = 0

    while guess != val:
        tries += 1
        guess = (high - low) / 2 + low
        if val > guess:
            low = guess
        if val < guess:
            high = guess

    return tries


def is_palindrome_anagram(word):
    """ Checks if word is anagram of plaindrome

    >>> is_palindrome_anagram("a")
    True

    >>> is_palindrome_anagram("ab")
    False

    >>> is_palindrome_anagram("aab")
    True

    >>> is_palindrome_anagram("arceace")
    True

    >>> is_palindrome_anagram("arceaceb")
    False
    """

    # Palindromes need to have even counts for each letter
    # At most one letter has an odd count
    # Go through each letter of word and update a count dict
    # Check that not more than one letter has an odd count
    letter_count = {}

    for letter in word:
        # This defaults letter count to 0 if letter not in dict yet
        letter_count[letter] = letter_count.get(letter, 0) + 1

    odd_counts = 0
    for letter, count in letter_count.iteritems():
        if count % 2 != 0:
            odd_counts += 1

        if odd_counts > 1:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

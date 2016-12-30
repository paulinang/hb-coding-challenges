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

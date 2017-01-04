def lemur(branches):
    """ How many jumps to traverse branches
    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 0, 0, 0])
    2

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
    """

    jumps = 0
    current_branch = 0

    # Deal with just live branches first
    # While current branch is less that index of last branch
    while current_branch < len(branches) - 1:
        # Check if can jump 1 or 2 branches
        # If there is a branch to land on in a 2 branch jump
        # If current_branch + 2 is less or equal to index of last branch
        if (current_branch + 2) < len(branches) and branches[current_branch + 2] != 1:
            # Move up 2 branches
            current_branch += 2
        else:
            # Move up 1 branch
            current_branch += 1

        jumps += 1

    return jumps


def lemming_cafe(num_holes, cafes):
    """ Find biggest distance lemming has to travel from a hole to a cafe
    >>> lemming_cafe(6, [2, 4])
    2
    >>> lemming_cafe(5, [0])
    4
    >>> lemming_cafe(10, [2, 3])
    6
    """

    first_distance = cafes[0]
    last_distance = num_holes - 1 - cafes[-1]
    max_distance = max(first_distance, last_distance)
    for i in range(len(cafes) - 1):
        dist_between_cafes = cafes[i + 1] - cafes[i]
        max_distance - max(max_distance, round(dist_between_cafes/2.0))

    return max_distance


def decode(s):
    """ Decode a string that gives # to skip, buffer letters, actual letter
    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'
    """
    message = ''
    i = 0
    while i < len(s) - 1:
        skip = int(s[i])
        message = message + s[i + skip + 1]
        i = i + skip + 2

    return message


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

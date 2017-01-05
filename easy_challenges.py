def sum_list(nums):
    """ Recursively sum list of nums
    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

    >>> sum_list([])
    0
    """

    if nums:
        return nums[0] + sum_list(nums[1:])

    return 0


def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']
    """

    items = []
    # go through each char in astring
    # append to a new string
    # check if next few chars are splitter
    # if yes, append new string to items and start new string
    # start checking chars after splitter
    item = ''
    i = 0
    while i < len(astring):
        if splitter == astring[i: i + len(splitter)]:
            items.append(item)
            item = ''
            i += len(splitter) - 1
        else:
            item += astring[i]

        i += 1

    items.append(item)
    return items


def sort_ab(a, b):
    """ Return sorted list containing items of a and b

    >>> a = [1, 3, 5, 7]
    >>> b = [2, 6, 8, 10]
    >>> sort_ab(a, b)
    [1, 2, 3, 5, 6, 7, 8, 10]
    """

    ab = []
    # Go through a and b one at a time comparing which is smaller
    i = 0
    j = 0
    # while (i < len(a)) or (j < len(b)):
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ab.append(a[i])
            i += 1
        else:
            ab.append(b[j])
            j += 1
    if i == len(a):
        ab.extend(b[j:])
    else:
        ab.extend(a[i:])

    return ab


def show_evens(nums):
    """Return list of indices for even nums

    >>> lst = [1, 2, 3, 4, 6, 8]
    >>> show_evens(lst)
    [1, 3, 4, 5]

    >>> show_evens([])
    []

    >>> show_evens([1, 3, 5])
    []

    >>> show_evens([2, 4, 6, 7])
    [0, 1, 2]
    """

    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def rev_string(astring):
    """Return reverse of string using recursion.

    >>> rev_string('')
    ''

    >>> rev_string('a')
    'a'

    >>> rev_string('ah')
    'ha'

    >>> rev_string("porcupine")
    'enipucrop'
    """

    if len(astring) == 0:
        return ''

    return astring[-1] + rev_string(astring[:-1])


def dedupe(items):
    """ Remove duplicates from list while keeping order. Return in new list
    >>> dedupe([1, 1, 1])
    [1]

    >>> dedupe([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> dedupe([1, 2, 3])
    [1, 2, 3]

    >>> a = [1, 2, 3]
    >>> b = dedupe(a)
    >>> a == b
    True

    >>> a is b
    False

    >>> dedupe([])
    []
    """

    unique = set(items)
    new_lst = []
    for item in items:
        if item in unique:
            new_lst.append(item)
            unique.remove(item)

    return new_lst


def recursive_search(target, items, start=0):
    """ Search for target in list of items recursively
    >>> lst = ["hey", "there", "you"]
    >>> recursive_search("hey", lst)
    0

    >>> recursive_search("you", lst)
    2

    >>> recursive_search("porcupine", lst) is None
    True
    """
    if len(items) == 0:
        return None

    if target == items[0]:
        return start

    return recursive_search(target, items[1:], start + 1)


def print_recursively(items):
    """ Print each item of list using recursion
    >>> print_recursively([1, 2, 3])
    1
    2
    3
    """
    if len(items) == 0:
        return

    print items[0]
    print_recursively(items[1:])


def print_digits(num):
    """ Print each digit in reverse, not using string reversal
    >>> print_digits(1)
    1

    >>> print_digits(314)
    4
    1
    3

    >>> print_digits(12)
    2
    1

    """
    while num > 0:
        print num % 10
        num = num // 10


def primes(count):
    """ Return count number of primes starting at 2
    >>> primes(0)
    []
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    >>> primes(7)
    [2, 3, 5, 7, 11, 13, 17]
    """
    prime_nums = []
    i = 0
    num = 0
    while i < count:
        while not is_prime(num):
            num += 1
        prime_nums.append(num)
        i += 1
        num += 1

    return prime_nums


def is_prime(num):
    """ Helper function to check if num is prime
    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True
    """

    if num < 2:
        return False
    else:
        i = num - 1
        while i > 1:
            if num % i == 0:
                return False
            i -= 1
        return True


def pig_latin(phrase):
    """ Pig latinize a phrase with no punctuation
    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'
    """

    vowels = 'aeiou'
    new_words = []
    for word in phrase.split():
        if not word[0] in vowels:
            new_words.append(word[1:] + word[0] + 'ay')
        else:
            new_words.append(word + 'yay')

    return ' '.join(new_words)


def is_pangram(sentence):
    """ Does sentence contain all letters of alphabet?
    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False
    """
    sentence_alphabets = set([])
    for char in sentence:
        if char.isalpha():
            sentence_alphabets.add(char.lower())

    # Using set comprehension, but linter detects error that DNE
    # sentence_alphabets = {char.lower() for char in sentence if char.isalpha()}
    return len(sentence_alphabets) == 26


def missing_num(nums, max_num):
    """ Find missing number in list from 1 to max_num
    >>> missing_num([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """
    return sum(range(1, max_num + 1)) - sum(nums)
    #return (set(range(1, max_num + 1)) - set(nums)).pop()


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

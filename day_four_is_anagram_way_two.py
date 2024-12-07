from collections import Counter


def normalized_string(input_string: str) -> str:
    """
    Normalize a string by stripping whitespace, removing spaces, 
    and converting to lowercase.
    """
    return input_string.strip().replace(" ", "").lower()


def is_anagram(string_one: str, string_two: str) -> bool:
    """
    Checks if two strings are anagrams of each other.

    Args:
        string_one: The first string.
        string_two: The second string.

    Returns: 
        True if the strings are anagrams, False otherwise.
    """

    # Normalize the input strings
    string_one = normalized_string(string_one)
    string_two = normalized_string(string_two)

    # If lengths differ, they cannot be anagrams
    if len(string_one) != len(string_two):
        return False

    if Counter(string_one) != Counter(string_two):
        return False

    return True


print(is_anagram("hello", "Helllooo"))  # False
print(is_anagram("hello", "ollhe"))  # True
print(is_anagram("qq", "qqq"))  # False
print(is_anagram("qqb", "qqq"))  # False

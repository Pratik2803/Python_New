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

    dict_string_one = {}
    for char in string_one:
        dict_string_one[char] = dict_string_one.get(char, 0) + 1

    dict_string_two = {}
    for char in string_two:
        dict_string_two[char] = dict_string_two.get(char, 0) + 1

    if dict_string_one != dict_string_two:
        return False

    return True


print(is_anagram("hello", "Helllooo"))
print(is_anagram("hello", "ollhe"))
print(is_anagram("qq", "qqq"))
print(is_anagram("qqb", "qqq"))

def is_anagram(str1, str2):
    """
    Check if two given strings are anagrams.

    Parameters:
    - str1 (str): First string
    - str2 (str): Second string

    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(str1) == sorted(str2)


# Example usage:
word1 = "listen"
word2 = "silent"
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

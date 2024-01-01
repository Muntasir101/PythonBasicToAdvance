def shortest_word(sentence):
    """
    Find the shortest word in a given sentence.

    Parameters:
    - sentence (str): Input sentence

    Returns:
    str: Shortest word in the sentence.
    """
    words = sentence.split()
    return min(words, key=len)


# Example usage:
input_sentence = "This is a sample sentence with short words."
result = shortest_word(input_sentence)
print(f"The shortest word is: {result}")

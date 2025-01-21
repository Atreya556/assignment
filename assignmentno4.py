def my_split(sentence, separator):
    """
    Splits a sentence into a list of words using the given separator.

    Args:
        sentence: The sentence to be split.
        separator: The character used to separate words.

    Returns:
        A list of words.
    """
    words = []
    current_word = ""
    for char in sentence:
        if char == separator:
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    if current_word:  
        words.append(current_word)
    return words

def my_join(word_list, separator):
    """
    Joins a list of words into a single string using the given separator.

    Args:
        word_list: The list of words to be joined.
        separator: The character used to separate words.

    Returns:
        A string of joined words.
    """
    joined_string = ""
    for i, word in enumerate(word_list):
        joined_string += word
        if i < len(word_list) - 1:  
            joined_string += separator
    return joined_string


sentence = input("Please enter sentence:")

split_words = my_split(sentence, " ")


joined_sentence = my_join(split_words, ",")


print(joined_sentence)
for word in split_words:
    print(word)
from data_structures.hashtable import Hashtable

def first_repeated_word(text):
    word_count = {}
    words = text.lower().split()

    for word in words:
        cleaned_words = ''.join(char if char.isalnum() or char == '-' else ' ' for char in word).split()

        for cleaned_word in cleaned_words:
            if cleaned_word in word_count:
                return cleaned_word
            word_count[cleaned_word] = 1

    return None


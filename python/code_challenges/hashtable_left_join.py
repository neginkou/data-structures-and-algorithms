from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    """
    Perform a LEFT JOIN on two hashmaps.

    Args:
    - synonyms (dict): A dictionary where keys are words and values are synonyms.
    - antonyms (dict): A dictionary where keys are words and values are antonyms.

    Returns:
    - list: A list of lists where each inner list contains the key from the first hashmap,
      the value from the first hashmap, and the value from the second hashmap (or 'NONE' if no
      value exists in the second hashmap).
    """
    result = []
    for word, synonym in synonyms.items():
        antonym = antonyms.get(word, 'NONE')
        result.append([word, synonym, antonym])
    return result

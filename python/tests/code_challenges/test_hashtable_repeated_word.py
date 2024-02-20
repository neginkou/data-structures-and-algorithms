import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word


def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


def first_repeated_word(text):
    word_count = {}
    words = text.lower().split()

    for word in words:
        cleaned_words = ''.join(char if char.isalnum() or char == ' ' else ' ' for char in word).split()

        for cleaned_word in cleaned_words:
            if cleaned_word in word_count:
                return cleaned_word
            word_count[cleaned_word] = 1

    return None

from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(input_string):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in input_string:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False

    return stack.is_empty()

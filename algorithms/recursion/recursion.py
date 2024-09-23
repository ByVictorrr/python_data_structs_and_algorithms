from statistics import median
from typing import Union, List


def digit_sum(num: int) -> int:
    """Recursively computes the sum of digits of the given integer.

    If the number is positive:
        digit_sum(1729) -> 1 + 7 + 2 + 9 = 19

    If the number is negative:
        The function returns the negation of the sum of the digits.
        digit_sum(-1729) -> - (1 + 7 + 2 + 9) = -19

    :param num: The integer for which to compute the sum of digits.
    :type num: int

    :return: The sum of the digits, preserving the sign of the original number.
    :rtype: int
    """
    if num == 0:
        return 0
    if num < 0:
        return -digit_sum(-num)
    return num % 10 + digit_sum(num // 10)


def stutter_stack(stack: list[int]):
    """Recursively replaces each element in the stack with two occurrences of that value.

    Given a stack `s` (represented as a list of integers), the function modifies the stack in place such that each
    value appears twice consecutively.

    Example:
        s = [1, 2, 3]
        stutter_stack(s)
        After the function call, `s` will be [1, 1, 2, 2, 3, 3].

    :param stack: A stack of integers to be modified in place.
    :type stack: list[int]

    :return: None. The stack is modified in place.
    :rtype: None
    """
    # function implementation goes here
    if len(stack) == 0:
        return
    value = stack.pop()
    stutter_stack(stack)
    stack.append(value)
    stack.append(value)


def reverse_text(text: str):
    if not text:
        return text
    return text[-1] + reverse_text(text[:-1])


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def is_palindrome(text: str):
    if not text:
        return True
    if len(text) == 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def count_leaf_items(item_list: Union[str, List]):
    count = 0
    for item in item_list:
        if isinstance(item_list, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count


def quicksort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
    items_less, pivot_items, items_greater = (
        [n for n in numbers if n < pivot],
        [n for n in numbers if n == pivot],
        [n for n in numbers if n > pivot]
    )
    return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
    )


if __name__ == "__main__":
    names = [
        "Adam",
        [
            "Bob",
            [
                "Chet",
                "Cat",
            ],
            "Barb",
            "Bert"
        ],
        "Alex",
        [
            "Bea",
            "Bill"
        ],
        "Ann"
    ]
    count_leaf_items(names)

    pass

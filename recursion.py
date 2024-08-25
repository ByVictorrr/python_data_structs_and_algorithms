from sys import getrecursionlimit, setrecursionlimit
from statistics import median


def example_of_recursion_error():
    """Show that recursion will keep going."""
    x = 10
    example_of_recursion_error()


def countdown(n):
    print(n)
    if n == 0:  # terminate recursion
        return
    else:
        countdown(n - 1)  # recursive call


def countdown_iterative(n):
    while n >= 0:
        print(n)
        n -= 1


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def count_leaf_items(item_list):
    count = 0
    for item in item_list:
        if isinstance(item_list, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count


def is_palindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


def quicksort(numbers):
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
    print("-" * 16 + "Recursion Examples" + "-" * 16)
    try:
        example_of_recursion_error()
    except RecursionError as err:
        print(f"Recursion limit of {getrecursionlimit()} reached")
    print("-" * 50)
    print("Count down to Zero")
    countdown(5)
    print("-" * 50)
    print("Factorial")
    factorial(10)
    print("-" * 50)
    print("Traverse a Nested List Recursively")
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
    print(count_leaf_items(names))
    print("-" * 50)
    print("Recursive Palindrome")
    print(f"cheer={is_palindrome('cheer')}")
    print(f"racecar={is_palindrome('racecar')}")
    print("-" * 50)
    print("Quicksort")
    q_list = [10, -3, 21, 6, -8]
    print(f"{q_list} -> {quicksort(q_list)}")
    print("-" * 50)

import random
import string
from pygtrie import CharTrie
import nltk
from nltk.corpus import words


def make_change(amount: int, coins: list[int]):
    def _make_change(_amount: int, _coins: list[int], current_solution: list[int] = None, coin_index: int = 0):
        """Recursively calculates and prints all possible ways to make the given amount of change using an unlimited supply
        of the provided coin denominations.

        The function should print a list representing the number of each coin used to make the given amount, based on the
        denominations in the `coins` list. Each recursive call represents a different combination of coins.

        :param _amount: The total amount of change to make (in cents).
        :type _amount: int

        :param _coins: A list of available coin denominations (in cents).
        :type _coins: list[int]

        :param current_solution: A list that tracks the current number of each coin used. Defaults to an empty list or None.
        :type current_solution: list[int], optional

        :param coin_index: The current index in the coins list being used for the solution. Defaults to 0.
        :type coin_index: int, optional

        :return: None. This function prints each valid combination of coins that sum to the given amount.
        """
        if _amount == 0:
            print(f"sum = {current_solution} = {sum(current_solution)}")
            return
        if coin_index >= len(_coins) or _amount < 0:
            return

        coin = _coins[coin_index]
        # Explore 1: include the current coin
        _make_change(_amount - coin, _coins, current_solution + [coin], coin_index)
        # Explore 2: exclude the current coin
        _make_change(_amount, _coins, current_solution, coin_index + 1)

    return _make_change(amount, coins, [], 0)


def is_measurable(weights: set[int], target: int) -> bool:
    """Recursively determines whether it is possible to weigh out exactly a given amount on two scales,
    using the provided weights.

    The function explores all possible combinations of adding or subtracting the weights from a target
    amount to check if the exact target weight can be measured.

    Example:
        weights = {1, 3}
        is_measurable(weights, 4) -> True
        is_measurable(weights, 2) -> True
        is_measurable(weights, 5) -> False

    :param weights: A list of integers representing the available weights.
    :type weights: set[int]

    :param target: The target amount of weight to measure.
    :type target: int

    :return: True if the target can be measured using the available weights, False otherwise.
    :rtype: bool
    """
    # base case
    if len(weights) == 0:
        return target == 0

    # recursive case
    curr = weights.pop()
    val = (
            is_measurable(weights, target - curr) or
            is_measurable(weights, target + curr) or
            is_measurable(weights, target)
    )
    weights.add(curr)
    return val


def password_checker():
    # Generate a random password
    password_length = 12
    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))

    def _check_password(input_password):
        """Check if the input password matches the generated password."""
        return input_password == generated_password

    return _check_password


check_password = password_checker()


def crack(max_length: int) -> bool:
    def crack_helper(max_length: int, current: str) -> bool:
        """Uses recursive backtracking to search for the correct password by exhaustively generating all possible strings
        of letters (both lowercase and uppercase) up to the given length. The function calls the `login` function to
        check if the generated string is the correct password. If the correct password is found, it returns the password.
        Otherwise, if no password matches, it returns an empty string.

        The password consists of letters from 'a' to 'z' and 'A' to 'Z', and the function tries all possible combinations
        up to the specified length, searching for the right password.

        Example:
            crack(4) -> "ViVa"
            crack(3) -> ""  (returns empty because no 1-3 letter password would match "ViVa")

        :param max_length: The maximum length of the password to be tested. The function will try passwords
                           of lengths from 1 to max_length. If max_length is 0, the function returns an empty string.
        :type max_length: int

        :return: The correct password if found, or an empty string if no correct password is found.
        :rtype: str

        :raises ValueError: If the max_length is negative, the function raises a ValueError.
        """

        if check_password(current):
            return True
        # base case
        if max_length < len(current):
            return False
        if max_length == 0:
            return False
        if max_length < 0:
            raise ValueError("Make sure max_length > 0")
        # recursive case
        for ch in string.ascii_lowercase + string.ascii_uppercase:
            if crack_helper(max_length, current + ch):
                return True
        return False

    return crack_helper(max_length, "")


def list_permutations(text: str):
    def list_permutations_helper(remaining, so_far):
        if not remaining:
            print(so_far)
            return
        for i in range(len(remaining)):
            next_choice = remaining[i]
            # Exclude the i-th character
            new_remaining = remaining[:i] + remaining[i + 1:]
            list_permutations_helper(new_remaining, so_far + next_choice)

    return list_permutations_helper(text, "")


def is_shrinkable(word: str):
    nltk.download("words")
    trie = CharTrie()
    for w in words.words():
        trie[w] = True

    def is_shrinkable_helper(remaining, so_far):
        if len(remaining) == 1 and trie.has_node(remaining):
            return True
        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i + 1:]
            if is_shrinkable_helper(new_remaining, so_far + remaining[i]):
                return True
        return False

    return is_shrinkable_helper(word, "")


def find_all_subsets(values: list[str]):
    def find_all_subsets_helper(remaining: list, chosen: set):
        if not remaining:
            print(f"{chosen}")
            return
        # Step 1 - choose
        elem = remaining[0]
        remaining = remaining[1:]
        # Step 2 - Explore: don't include the element
        find_all_subsets_helper(remaining, chosen)
        chosen.add(elem)
        # Step 3 - Explore: include the element
        find_all_subsets_helper(remaining, chosen)
        # Step 4 - un-choose
        chosen.remove(elem)
        remaining.append(elem)

    return find_all_subsets_helper(values, set())


def find_all_combinations(graders: set[str], comb_size: int) -> set[set[str]]:
    combinations = set()

    def find_all_combinations_helper(remaining: set[str], k: int, chosen: set[str]) -> set[set[str]]:
        # Base Case: when k is 0 then we have reached the constraint
        if k == 0:
            combinations.add(frozenset(chosen))
        for grader in remaining:
            # Exclude the i-th character
            remaining.remove(grader)
            chosen.add(grader)
            find_all_combinations_helper(remaining, k - 1, chosen)
            remaining.add(grader)
            chosen.remove(grader)
        return combinations

    return find_all_combinations_helper(graders, comb_size, set())


if __name__ == "__main__":
    # values = find_all_combinations({"Vic", "Dan", "Mark"}, 2)
    # print(f"{values}")
    # find_all_subsets(["Jenny", "Kylie", "Trip"])
    # list_permutations("cat")
    # print(f'{is_shrinkable("cart")=}')
    make_change(15, [1, 5, 10])

    pass

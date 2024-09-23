from python_data_structs_and_algorithms.algorithms.recursion import stutter_stack, digit_sum, reverse_text, is_palindrome, is_measurable, crack, make_change


def test_digit_sum():
    """Tests the digit_sum function with multiple test cases."""
    # Generate a list of test cases with negative and non-negative inputs
    test_cases = [-1729, 1729, -123, 123, -4567, 4567, 0, -9, 9]

    # Expected outputs for the test cases
    expected_outputs = [-19, 19, -6, 6, -22, 22, 0, -9, 9]

    # Loop through the test cases and assert the results
    for num, expected in zip(test_cases, expected_outputs):
        result = digit_sum(num)
        assert result == expected, f"Test failed for {num}: got {result}, expected {expected}"
        print(f"Test passed for {num}: {result}")

    print("All test cases passed for digit_sum!")


def test_stutter_stack():
    """Tests the stutter_stack function with multiple test cases."""

    # Test case 1: Basic case
    s = [1, 2, 3]
    stutter_stack(s)
    expected = [1, 1, 2, 2, 3, 3]
    assert s == expected, f"Test case 1 failed: got {s}, expected {expected}"

    # Test case 2: Empty stack
    s = []
    stutter_stack(s)
    expected = []
    assert s == expected, f"Test case 2 failed: got {s}, expected {expected}"

    # Test case 3: Stack with one element
    s = [5]
    stutter_stack(s)
    expected = [5, 5]
    assert s == expected, f"Test case 3 failed: got {s}, expected {expected}"

    # Test case 4: Stack with duplicate elements
    s = [4, 4, 6]
    stutter_stack(s)
    expected = [4, 4, 4, 4, 6, 6]
    assert s == expected, f"Test case 4 failed: got {s}, expected {expected}"

    # Test case 5: Stack with negative numbers
    s = [-1, -2, -3]
    stutter_stack(s)
    expected = [-1, -1, -2, -2, -3, -3]
    assert s == expected, f"Test case 5 failed: got {s}, expected {expected}"

    print("All test cases passed for stutter_stack!")


def test_is_measurable():
    """Tests the is_measurable function with various cases."""

    # Test case 1: Target can be measured with the given weights
    weights = {1, 3}
    assert is_measurable(weights, 4), f"Test case 1 failed: expected True but got {is_measurable(weights, 4)}"

    # Test case 2: Target can be measured with the given weights
    weights = {1, 3}
    assert is_measurable(weights, 2), f"Test case 2 failed: expected True but got {is_measurable(weights, 2)}"

    # Test case 3: Target cannot be measured with the given weights
    weights = {1, 3}
    assert not is_measurable(weights, 5), f"Test case 3 failed: expected False but got {is_measurable(weights, 5)}"

    # Test case 4: Target can be measured as 0
    weights = {1, 3}
    assert is_measurable(weights, 0), f"Test case 4 failed: expected True but got {is_measurable(weights, 0)}"

    # Test case 5: Larger weights
    weights = {1, 3, 7}
    assert is_measurable(weights, 10), f"Test case 5 failed: expected True but got {is_measurable(weights, 10)}"

    # Test case 6: Impossible target with larger weights
    weights = {1, 3, 7}
    assert is_measurable(weights, 6), f"Test case 6 failed: expected False but got {is_measurable(weights, 6)}"

    print("All test cases passed for is_measurable!")


# Simulated login function for testing
def test_reverse_text():
    """
    Test the reverse_text function by verifying the following cases:

    1. Reversing a standard string "hello" should return "olleh".
    2. Reversing an empty string should return an empty string.
    3. Reversing a single-character string should return the same character.
    4. Reversing a palindrome should return the same string.
    """
    assert reverse_text("hello") == "olleh", "Test Case 1 Failed"
    assert reverse_text("") == "", "Test Case 2 Failed"
    assert reverse_text("a") == "a", "Test Case 3 Failed"
    assert reverse_text("madam") == "madam", "Test Case 4 Failed"
    print("All reverse_text test cases passed.")


def test_is_palindrome():
    """
    Test the is_palindrome function by verifying the following cases:

    1. "madam" is a palindrome, so the function should return True.
    2. "hello" is not a palindrome, so the function should return False.
    3. An empty string is considered a palindrome, so it should return True.
    4. A single-character string is considered a palindrome, so it should return True.
    """
    assert is_palindrome("madam") == True, "Test Case 1 Failed"
    assert is_palindrome("hello") == False, "Test Case 2 Failed"
    assert is_palindrome("") == True, "Test Case 3 Failed"
    assert is_palindrome("a") == True, "Test Case 4 Failed"
    print("All is_palindrome test cases passed.")


def test_crack():
    """Tests the crack function with different cases."""

    # Test case 1: Max length 4 should return True (able to find the correct password "ViVa")
    assert crack(12), f"Test case 1 Passed: expected True, got {crack(12)}"

    # Test case 2: Max length 3 should return False (unable to find the correct password with max length 3)
    assert not crack(12), f"Test case 2 failed: expected False, got {crack(3)}"

    # Test case 3: Max length 0 should return False (no passwords of length 0 can be valid)
    assert not crack(0), f"Test case 3 failed: expected False, got {crack(0)}"

    # Test case 4: Negative max length should raise a ValueError
    try:
        crack(-1)
    except ValueError:
        print("Test case 4 passed: correctly raised ValueError for negative max length.")
    else:
        print("Test case 4 failed: did not raise ValueError for negative max length.")

    # Test case 5: Max length 5 should return True (should still be able to crack the correct password "ViVa")
    assert crack(5), f"Test case 5 failed: expected True, got {crack(5)}"

    print("All test cases passed on crack!")


if __name__ == "__main__":
    test_reverse_text()
    test_is_palindrome()
    test_digit_sum()
    test_stutter_stack()
    test_is_measurable()
    # test_crack()
    make_change(15, [1, 5, 3])

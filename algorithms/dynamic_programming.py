def fib_r(n):
    """Recursive approach to calculate the nth fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_r(n - 1) + fib_r(n - 2)


def fib_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]


def fib_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


if __name__ == "__main__":

    pass
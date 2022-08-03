"""
Dynamic Programming = Memoization + Tabulation
ask (c) 2022. All rights reserved.
"""


def fib(n) -> int:
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_dp(n, memo={}) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1
    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


# print(fib(50))
print(fib_dp(50))

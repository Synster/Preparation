"""

ask (c) 2022. All rights reserved.
"""


def fib(n):
    sequence = [0] * (n + 3)  # we only need array of n+1 adding extra 2 elements to avoid outofbound exception
    sequence[1] = 1
    for i in range(n + 1):
        sequence[i + 1] += sequence[i]
        sequence[i + 2] += sequence[i]

    return sequence[n]


def fact(n):
    sequence = [1] * (n + 1)  # we only need array of n+1
    sequence[0] = 1
    for i in range(1, n + 1):
        sequence[i] = i * sequence[i - 1]

    return sequence[n]


print(fib(6))
print(fact(4))
print(fib(50))

"""

target_sum -> m-> height of tree in worst case
len(numbers) -> n -> branching factor

complexity brute force -> O(n^m)
Space Complexity -> O(m)

Optimised

time complexity -> O(m*n)
Space Complexity -> O(m)

ask (c) 2022. All rights reserved.
"""


def can_sum(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        result = can_sum(target_sum - num, numbers, memo)
        if result:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3, 4, 5, 7], {}))
print(can_sum(300, [7, 14], {}))

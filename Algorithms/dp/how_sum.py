"""

target_sum -> m-> height of tree in worst case
len(numbers) -> n -> branching factor

complexity brute force -> O(n^m*m)
Space Complexity -> O(m)

Optimised

time complexity -> O(m*n*m) -> O(m*n^2)
Space Complexity -> O(m^2)

ask (c) 2022. All rights reserved.
"""


def how_sum(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        result = how_sum(target_sum - num, numbers, memo)

        if result is not None:
            result = result.copy()
            result.append(num)
            memo[target_sum] = result
            return result

    memo[target_sum] = None
    return None


print(how_sum(7, [2, 3, 4], {}))
print(how_sum(7, [3, 4], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(300, [5, 10], {}))
print(how_sum(300, [7, 14], {}))

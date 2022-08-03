"""

target_sum -> m-> height of tree in worst case
len(numbers) -> n -> branching factor

complexity brute force -> O(n^m*m)
Space Complexity -> O(m^2)

Optimised

time complexity -> O(m^2*n)
Space Complexity -> O(m^2)

ask (c) 2022. All rights reserved.
"""


def can_construct(target_string, strings, memo):
    if target_string in memo:
        return memo[target_string]

    if target_string == "":
        return True

    for s in strings:
        if not target_string.startswith(s):
            continue

        remaining_str = target_string[len(s):]
        if can_construct(remaining_str, strings, memo):
            memo[target_string] = True
            return True
    memo[target_string] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(can_construct("abcdef", ["ab", "abc", "cd", "df", "abcd"], {}))
print(can_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"], {}))

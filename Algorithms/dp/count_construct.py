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


def count_construct(target_string, word_bank, memo):
    if target_string in memo:
        return memo[target_string]
    if target_string == "":
        return 1
    count = 0
    for word in word_bank:
        if not target_string.startswith(word):
            continue
        suffix = target_string[len(word):]
        count += count_construct(suffix, word_bank, memo)

    memo[target_string] = count

    return count


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(count_construct("abcdef", ["ab", "abc", "cd", "df", "abcd"], {}))
print(count_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"], {}))

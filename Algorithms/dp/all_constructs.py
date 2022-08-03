"""

Complexity O(n^m)
Space O(m)

ask (c) 2022. All rights reserved.
"""


def all_constructs(target_string, word_bank, memo):
    if target_string in memo:
        return memo[target_string]

    if target_string == "":
        return [[]]

    all_results = []
    for word in word_bank:
        if not target_string.startswith(word):
            continue

        suffix = target_string[len(word):]
        result = all_constructs(suffix, word_bank, memo)

        for res in result:
            res = res.copy()
            res.insert(0, word)
            all_results.append(res)

    memo[target_string] = all_results
    return all_results


print(all_constructs('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {}))
print(all_constructs('purple', ['purp', 'le', 'pu', 'r', 'ple'], {}))
print(all_constructs('purple', ['purp', 'l', 'pu', 'ple'], {}))
print(all_constructs('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aa', 'aaaa', 'aaa', 'aaaaa'],
                     {}))  # Not the worst case

"""

ask (c) 2022. All rights reserved.
"""


def can_construct(target_string, words):
    table = [False for _ in range(len(target_string) + 1)]
    table[0] = True

    for i in range(len(target_string) + 1):
        if not table[i]:
            continue
        for word in words:

            if i + len(word) <= len(target_string) and target_string[i:i + len(word)] == word:
                table[i + len(word)] = True

    return table[len(target_string)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

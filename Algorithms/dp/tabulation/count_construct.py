"""

ask (c) 2022. All rights reserved.
"""


def count_construct(target_string, words):
    table = [0 for _ in range(len(target_string) + 1)]
    table[0] = 1

    for i in range(len(target_string) + 1):
        if table[i] == 0:
            continue
        for word in words:

            if i + len(word) <= len(target_string) and target_string[i:i + len(word)] == word:
                table[i + len(word)] += table[i]

    return table[len(target_string)]


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))  # 3

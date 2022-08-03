"""

ask (c) 2022. All rights reserved.
"""


def count_construct(target_string, words):
    table = [[] for _ in range(len(target_string) + 1)]
    table[0] =[[]]

    for i in range(len(target_string) + 1):
        if not table[i]:
            continue
        for word in words:

            if i + len(word) <= len(target_string) and target_string[i:i + len(word)] == word:
                for res in table[i]:
                    option = res.copy()
                    option.append(word)
                    table[i + len(word)].append(option)

    return table[len(target_string)]


print(count_construct("abcdef",
                      ["ab", "abc", "cd", "def", "abcd", "ef"]))  # [["ab", "cd", "ef"], ["abc", "def"], ["abcd", "ef"]]

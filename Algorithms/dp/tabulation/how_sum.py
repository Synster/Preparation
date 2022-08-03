"""

ask (c) 2022. All rights reserved.
"""


def how_sum(target_sum, numbers):
    table = [None for _ in range(target_sum + 1)]

    table[0] = []

    for i in range(target_sum):
        if table[i] is None:
            continue
        for num in numbers:
            if num + i <= target_sum:
                table[num + i] = table[i].copy()
                table[num + i].append(num)

    return table[target_sum]


print(how_sum(7, [2, 3, 4]))

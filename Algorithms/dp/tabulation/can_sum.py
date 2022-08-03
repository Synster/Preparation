"""

ask (c) 2022. All rights reserved.
"""


def can_sum(target_sum, numbers):
    table = [False for _ in range(target_sum + 1)]

    table[0] = True

    for i in range(target_sum + 1):

        if not table[i]:
            continue
        for num in numbers:
            if i + num <= target_sum:
                table[i + num] = True

    return table[target_sum]


print(can_sum(7, [2, 3, 4, 5, 7]))
print(can_sum(300, [7, 14]))

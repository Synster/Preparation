"""

ask (c) 2022. All rights reserved.
"""


def grid_traveller(r, c):
    table = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

    table[1][1] = 1

    for i in range(r + 1):
        for j in range(c + 1):
            if i + 1 <= r:
                table[i + 1][j] += table[i][j]
            if j + 1 <= c:
                table[i][j + 1] += table[i][j]

    return table[r][c]


print(grid_traveller(3, 3))
print(grid_traveller(18, 18))

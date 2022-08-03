"""

ask (c) 2022. All rights reserved.
"""


def grid_traveller(m, n, memo={}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    if (m, n) in memo:
        return memo[(m, n)]

    memo[(m, n)] = grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
    return memo[(m, n)]


print(grid_traveller(1, 1))  # 1
print(grid_traveller(2, 3))  # 3
print(grid_traveller(3, 2))  # 3
print(grid_traveller(3, 3))  # 6
print(grid_traveller(18, 18))  # 2333606220

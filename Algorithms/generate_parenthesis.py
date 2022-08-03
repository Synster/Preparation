"""

ask (c) 2022. All rights reserved.
"""


def generate_parenthesis(n):
    def generate(n, diff, comb, combs):

        if diff < 0 or diff > n:
            return
        elif n == 0 and diff == 0:
            combs.append(''.join(comb))

        else:

            comb.append('(')
            generate(n - 1, diff + 1, comb, combs)

            comb.pop()
            comb.append(')')
            generate(n - 1, diff - 1, comb, combs)
            comb.pop()

    combs = []

    generate(2 * n, 0, [], combs)

    return combs


print(generate_parenthesis(3))

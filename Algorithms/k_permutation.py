"""
n elements have n! permutations we are interested in kth

example n = 3  permutations  n! = 6 let k = 5

permutation

123     213     312
132     231     321

length of part = permutations / n
            = 6 / 3 -> 2
            k/part_length
            = 5 / 2 -> 2 so our answer is in 2nd part
ask (c) 2022. All rights reserved.
"""


def kth_permutation(n, k):
    result = []
    fact = [1] * (n + 1)
    unused = [i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    k -= 1
    while n > 0:
        part_length = fact[n] // n
        x = k // part_length

        result.append(unused[x])
        unused.pop(x)

        n -= 1
        k = k % part_length

    return result


print(kth_permutation(3, 5))
print(kth_permutation(4, 16))

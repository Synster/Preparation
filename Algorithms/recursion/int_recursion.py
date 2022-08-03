"""

ask (c) 2022. All rights reserved.
"""


def dec_to_binary(num, result=""):
    if num == 0:
        return result

    result = str(num % 2) + result
    return dec_to_binary(num // 2, result)


def sum_natural_num(num):
    if num == 0:
        return 0
    return num + sum_natural_num(num - 1)


print(dec_to_binary(11))
print(dec_to_binary(0))
print(sum_natural_num(10))
print(sum_natural_num(20))

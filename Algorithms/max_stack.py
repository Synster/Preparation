"""

ask (c) 2022. All rights reserved.
"""
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
stack = []
max_stack = []


def push(value):
    if not stack:
        stack.append(value)
        max_stack.append(value)
        return

    top = max_stack[-1]
    if value > top:
        max_stack.append(value)
    else:
        max_stack.append(top)
    stack.append(value)


def pop():
    if not stack:
        return
    stack.pop()
    max_stack.pop()


def max_value():
    return max_stack[-1]


def getMax(operations):
    # Write your code here
    result = []
    for i in operations:
        if i.startswith('1'):
            o, value = i.split(" ")
            push(int(value))
        elif i.startswith('2'):
            pop()
        else:
            result.append(max_value())
    return result


if __name__ == '__main__':
    n = int(input().strip())

    ops = ["1 1",
           "1 44",
           "3",
           "3",
           "2",
           "3",
           "3",
           "1 3",
           "1 37",
           "2",
           "3",
           "1 29",
           "3",
           "1 73",
           "1 51",
           "3",
           ]

    res = getMax(ops)

    print(res)

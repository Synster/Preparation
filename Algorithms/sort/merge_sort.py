"""
Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach,
a powerful algorithmic technique used to solve complex problems.

Complexity O(nlogn)
Pros
    very efficient
    easy to parallelize
Cons
    memory inefficient
    may not be efficient of smaller lists

ask (c) 2022. All rights reserved.
"""


def merge(left, right):
    n = len(left)
    m = len(right)

    if n == 0:
        return right

    if m == 0:
        return left

    result = []
    i = j = 0

    while i < n and j < m:

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        result += left[i:]

    if j < m:
        result += right[j:]

    return result


def merge_sort(numbers):
    n = len(numbers)
    if n < 2:
        return numbers

    mid = n // 2

    left = merge_sort(numbers[: mid])

    right = merge_sort(numbers[mid:])

    return merge(left, right)


print(merge_sort([5, 4, 3, 2, 1]))

print(merge_sort([1, 2, 3, 4, 5]))

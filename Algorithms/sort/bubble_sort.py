"""
Bubble Sort is one of the most straightforward sorting algorithms.
Its name comes from the way the algorithm works:
With every new pass, the largest element in the list “bubbles up” toward its correct position.

Bubble sort consists of making multiple passes through a list, comparing elements one by one, and
swapping adjacent items that are out of order.

Complexity O(n^2)
Best Case O(n)
ask (c) 2022. All rights reserved.
"""


def bubble_sort(numbers):
    n = len(numbers)

    for i in range(0, n):
        already_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                already_sorted = False

        if already_sorted:
            break

    return numbers


print(bubble_sort([5, 4, 3, 2, 1]))

print(bubble_sort([1, 2, 3, 4, 5]))

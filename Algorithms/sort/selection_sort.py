"""

Complexity O(n^2)
ask (c) 2022. All rights reserved.
"""


def selection_sort(numbers):
    n = len(numbers)

    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):

            if numbers[min_index] > numbers[j]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


print(selection_sort([5, 4, 3, 2, 1]))

print(selection_sort([1, 2, 3, 4, 5]))

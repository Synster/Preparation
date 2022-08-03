"""
Unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and
inserting it into its correct position. This “insertion” procedure gives the algorithm its name.

Complexity O(n2)

insertion sort is considerably more efficient than bubble sort.

There are more powerful algorithms, including merge sort and Quicksort, but these implementations are recursive
and usually fail to beat insertion sort when working on small lists.

ask (c) 2022. All rights reserved.
"""


def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key_item = numbers[i]

        j = i - 1

        while j >= 0 and numbers[j] > key_item:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key_item
    return numbers


def insertion_sort2(nums):
    n = len(nums)

    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j]:
                nums[i], nums[j], = nums[j], nums[i]

    return nums


print(insertion_sort2([5, 4, 3, 2, 1]))

print(insertion_sort2([1, 2, 3, 4, 5]))

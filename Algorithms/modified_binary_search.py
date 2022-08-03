"""
Find first and last index of a number in a given list
ask (c) 2022. All rights reserved.
"""


def find_first(target, numbers):
    start = 0
    end = len(numbers)

    while start <= end:
        mid = start + (end - start) // 2

        if numbers[mid] == target and numbers[mid - 1] != target:
            return mid
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def find_last(target, numbers):
    start = 0
    end = len(numbers)

    while start <= end:
        mid = start + (end - start) // 2

        if numbers[mid] == target and numbers[mid + 1] != target:
            return mid
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def search(target, numbers):
    if not numbers:
        return [-1, -1]

    first = find_first(target, numbers)
    last = find_last(target, numbers)

    return [first, last]


print(search(5, [1, 1, 3, 4, 5, 5, 5, 5, 5, 7, 8, 9]))


# Search in a rotated sorted list
def search2(target, arr):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if target == arr[mid]:
            return mid
        # start ... mid is sorted
        if arr[start] <= arr[mid]:

            if arr[start] <= target <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:

            if arr[mid] <= target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


print(search2(5, [4, 5, 6, 7, 1, 2, 3]))

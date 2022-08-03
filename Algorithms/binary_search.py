"""
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to
O(Log n).

ask (c) 2022. All rights reserved.
"""


def binary_search(number, numbers) -> int:
    """
    >>> binary_search(5, [1,2,3,4,5,7,9])
    4
    >>> binary_search(10, [1,2,3,4,5,7,9])
    -1

    Searches the given number in a sorted list
    Args:
        number: number to be searched
        numbers: list of sorted numbers

    Returns:

    """
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if number == numbers[mid]:
            return mid
        elif number > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binary_search_recursive(number, numbers, start, end) -> int:
    """
    >>> binary_search_recursive(5, [1,2,3,4,5,7,9], 0, 6)
    4
    >>> binary_search_recursive(10, [1,2,3,4,5,7,9], 0, 6)
    -1

    Searches the given number in a sorted list
    Args:
        end: end index
        start: start index
        number: number to be searched
        numbers: list of sorted numbers

    Returns:

    """
    mid = start + (end - start) // 2

    if start > end:
        return -1

    if number == numbers[mid]:
        return mid
    elif number > numbers[mid]:
        return binary_search_recursive(number, numbers, mid + 1, end)
    else:
        return binary_search_recursive(number, numbers, start, mid - 1)

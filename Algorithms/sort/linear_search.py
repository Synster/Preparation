"""
Linear Search Approach: A simple approach is to do a linear search.
The time complexity of the Linear search is O(n).
Another approach to perform the same task is using Binary Search.

ask (c) 2022. All rights reserved.
"""


def linear_search(number, numbers) -> int:
    """
    >>> linear_search(5, [1,4,2,7,9,5])
    5
    >>> linear_search(10, [1,4,2,7,9,5])
    -1

    Searches the given number in a list
    Args:
        number: number to be searched
        numbers: list of numbers

    Returns:

    """
    for index, num in enumerate(numbers):
        if num == number:
            return index
    return -1



"""

ask (c) 2022. All rights reserved.
"""
import heapq


def find(k, numbers: list):
    """
    Remove k-1 max element, next max element is your answer
    """
    for _ in range(k - 1):
        numbers.remove(max(numbers))
    return max(numbers)


def find2(k, numbers: list):
    """
    Sort the numbers return -k element O(nlog(n))
    """
    numbers = sorted(numbers)
    return numbers[-k]


def find3(k, numbers: list):
    """
    Using priority Queue -> O(klogn), slightly better than sorting
    """
    numbers = sorted(numbers)
    return numbers[-k]


print(find(4, [1, 3, 5, 3, 2, 6, 7, 3, 9, 8, 6]))
print(find2(1, [1, 3, 5, 3, 2, 6, 7, 3, 9, 8, 6]))


class KlargestElement:
    import heapq

    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        if len(self.min_heap) >= self.k:
            heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, val)
        return self.min_heap[0]


x = KlargestElement(2, [1, 3])
print(x.add(2))
print(x.add(4))
print(x.add(7))
print(x.add(9))

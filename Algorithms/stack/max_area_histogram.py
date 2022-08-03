"""

ask (c) 2022. All rights reserved.
"""


def prev_smaller_element_index(arr):
    n = len(arr)
    result = [-1 for _ in range(n)]
    stack = [0]

    for i in range(1, n):

        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(i)

    return result


def next_smaller_element_index(arr):
    n = len(arr)
    result = [n for _ in range(n)]
    stack = [n-1]

    for i in range(n - 2, -1, -1):

        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else n

        stack.append(i)

    return result


def get_max_area(arr):
    left_smaller_element = prev_smaller_element_index(arr)
    right_smaller_element = next_smaller_element_index(arr)
    n = len(arr)
    max_area = 0
    for i in range(n):
        area = (right_smaller_element[i] - left_smaller_element[i] - 1) * arr[i]

        max_area = max(max_area, area)

    return max_area


# arr = [10, 4, 2, 20, 40, 12, 30]
# arr = [6, 2, 5, 4, 5, 1, 6]
# arr = [7, 2, 8, 9, 1, 3, 6, 5]
arr=[1, 2, 3, 4, 5]
print(arr)

print("Max Area: {}".format(get_max_area(arr)))

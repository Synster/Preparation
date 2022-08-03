"""

ask (c) 2022. All rights reserved.
"""


def prev_smallest_element(arr):
    n = len(arr)
    stack = [arr[0]]  # appending first element
    result = [-1 for _ in range(n)]
    for i in range(1, n):

        while stack and stack[-1] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(arr[i])
    return result


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


def prev_largest_element(arr):
    n = len(arr)
    stack = [arr[0]]  # appending first element
    result = [-1 for _ in range(n)]
    for i in range(1, n):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(arr[i])
    return result


def next_largest_element(arr):
    stack = [arr[-1]]
    n = len(arr)

    result = [-1 for _ in range(n)]

    for i in range(n - 2, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(arr[i])
    return result


def next_largest_element_index(arr):
    n = len(arr)
    result = [-1 for _ in range(n)]
    stack = [n - 1]

    for i in range(n - 2, -1, -1):

        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(i)

    return result


def next_smallest_element(arr):
    stack = [arr[-1]]
    n = len(arr)

    result = [-1 for _ in range(n)]

    for i in range(n - 2, -1, -1):

        while stack and stack[-1] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1

        stack.append(arr[i])
    return result


def stock_span_problem(arr):
    n = len(arr)
    stack = [arr[0]]  # appending first element
    result = [1 for _ in range(n)]
    for i in range(1, n):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        result[i] = i - arr.index(stack[-1]) if stack else i + 1

        stack.append(arr[i])
    return result


# Driver code
arr = [10, 4, 2, 20, 40, 12, 30]
print(arr)
print("Previous Smallest Element")
print(prev_smallest_element(arr))
print("Previous Smallest Element Index")
print(prev_smaller_element_index(arr))

print("Previous Largest Element")
print(prev_largest_element(arr))
print("Next Largest Element")
print(next_largest_element(arr))

print("Next Largest Element Index")
print(next_largest_element_index(arr))
print("Next Smallest Element")
print(next_smallest_element(arr))
print("Stock Span problem")
# Find the no of days for which the price of stock is less than the current
print(stock_span_problem(arr))

"""

ask (c) 2022. All rights reserved.
"""


def reverse(value):
    if not value:
        return value

    return reverse(value[1:]) + value[0]


def reverse_iterative(value):
    value = list(value)
    n = len(value)
    for i in range(n // 2):
        value[i], value[n - i - 1] = value[n - i - 1], value[i]

    return "".join(value)


def is_palindrome(value):
    value = list(value)
    n = len(value)
    for i in range(n // 2):
        if value[i] != value[n - i - 1]:
            return False

    return True


def is_palindrome_recursive(value):
    n = len(value)
    if n == 0 or n == 1:
        return True
    if value[0] == value[n - 1]:
        return is_palindrome_recursive(value[1:-1])

    return False


if __name__ == "__main__":
    print(reverse("Hello"))
    print(reverse_iterative("aman"))
    print(is_palindrome_recursive("aman"))
    print(is_palindrome_recursive("kayak"))

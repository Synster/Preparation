"""

ask (c) 2022. All rights reserved.
"""


class Stack:

    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if not self.arr:
            return None
        return self.arr.pop()

    def __str__(self):
        result = ""
        for i in range(len(self.arr) - 1, -1, -1):
            result += " {}".format(self.arr[i])
        return result


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)

stack.pop()
print(stack)

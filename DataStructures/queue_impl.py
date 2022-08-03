"""

ask (c) 2022. All rights reserved.
"""


class QueueImpl:

    def __init__(self):
        self.arr = []

    def enqueue(self, num):
        self.arr.append(num)

    def dequeue(self):
        if not self.arr:
            return None
        return self.arr.pop(0)

    def __str__(self) -> str:
        return ",".join(str(x) for x in self.arr)


q = QueueImpl()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

q.dequeue()
print(q)

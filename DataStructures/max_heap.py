"""

ask (c) 2022. All rights reserved.
"""


class MaxHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def has_left_child(self, index):
        return 2 * index <= self.size

    def has_right_child(self, index):
        return 2 * index + 1 <= self.size

    def get_max_child(self, index):
        if not self.has_right_child(index):
            return 2 * index

        if self.heap_list[2 * index] > self.heap_list[2 * index + 1]:
            return 2 * index
        return 2 * index + 1

    def shift_up(self, index):

        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]

            index = index // 2

    def shift_down(self, index):

        while index * 2 <= self.size:
            mc = self.get_max_child(index)

            if self.heap_list[mc] > self.heap_list[index]:
                self.heap_list[index], self.heap_list[mc] = self.heap_list[mc], self.heap_list[index]
            index = index * 2

    def insert(self, value):
        self.heap_list.append(value)
        self.size += 1
        self.shift_up(self.size)

    def remove(self):
        max_element = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1

        self.shift_down(1)
        return max_element


if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MaxHeap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)

    print("The max val is " + str(minHeap.remove()))
    print("The max val is " + str(minHeap.remove()))
    print("The max val is " + str(minHeap.remove()))
    print("The max val is " + str(minHeap.remove()))
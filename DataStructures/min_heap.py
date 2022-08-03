"""

ask (c) 2022. All rights reserved.
"""


class MinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def has_left_child(self, root_index):
        return 2 * root_index < self.current_size

    def has_right_child(self, root_index):
        return 2 * root_index + 1 < self.current_size

    def get_min_child_index(self, root_index):
        if not self.has_right_child(root_index):
            return 2 * root_index
        if self.heap_list[2 * root_index] < self.heap_list[2 * root_index + 1]:
            return 2 * root_index
        return 2 * root_index + 1

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.shift_up(self.current_size)

    def shift_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def shift_down(self, index):
        while index * 2 <= self.current_size:
            mc = self.get_min_child_index(index)

            if self.heap_list[index] > self.heap_list[mc]:
                self.heap_list[index], self.heap_list[mc] = self.heap_list[mc], self.heap_list[index]
            index = mc

    def peek(self):
        return self.heap_list[1]

    def delete_min(self):
        if self.current_size == 0:
            return "Empty Heap"

        min_element = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.shift_down(1)
        return min_element


if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)

    print("The Min val is " + str(minHeap.delete_min()))
    print("The Min val is " + str(minHeap.delete_min()))
    print("The Min val is " + str(minHeap.delete_min()))
    print("The Min val is " + str(minHeap.delete_min()))

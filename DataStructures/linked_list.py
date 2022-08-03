"""

ask (c) 2022. All rights reserved.
"""


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

    def print(self):
        print(self.value)

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:

    def __str__(self) -> str:
        linked_str = ""
        temp = self.head

        while temp:
            linked_str += "{} -> ".format(temp.value)
            temp = temp.next

        linked_str += "None"
        return linked_str

    def __init__(self):
        self.head = None

    def add_node(self, node: Node):
        if not self.head:
            self.head = node
            return self.head

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node

        return self.head

    def delete_node(self, node: Node):

        if not self.head:
            return self.head

        if self.head == node:
            self.head = self.head.next
            return self.head

        prev = self.head
        temp = self.head.next
        while prev.next:

            if temp.value == node.value:
                prev.next = temp.next
                return self.head

            prev = temp
            temp = temp.next

        return self.head

    def reverse(self):
        """

        Returns:

        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head

    def print(self):
        print(self)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node(Node(1))
    linked_list.add_node(Node(2))
    linked_list.add_node(Node(3))
    linked_list.add_node(Node(4))
    linked_list.add_node(Node(5))
    linked_list.add_node(Node(6))

    linked_list.print()
    linked_list.reverse()
    linked_list.print()
    linked_list.delete_node(Node(5))

    linked_list.print()

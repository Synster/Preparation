"""

ask (c) 2022. All rights reserved.
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


def _insert_node(val):
    pass


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            _insert_node(val)

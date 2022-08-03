"""

ask (c) 2022. All rights reserved.
"""
import sys


class Node:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

    def print(self):
        print(self.value)

    def __str__(self) -> str:
        return str(self.value)


def insert(root, val):
    if not root:
        root = Node(val)
        return root

    if val == root.value:
        return root
    elif val < root.value:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def search(root, val):
    if not root or val == root.value:
        return root
    elif val < root.value:
        return search(root.left, val)
    else:
        return search(root.right, val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value)
        inorder(root.left)
        inorder(root.right)


def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.value)


def dfs(root):
    if not root:
        return []
    print(root.value)
    left = dfs(root.left)
    right = dfs(root.right)

    result = [root.value]
    result.extend(left)
    result.extend(right)
    return result


def dfs_stack(root):
    if not root:
        return
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value)
        result.append(current.value)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


def bfs_queue(root):
    if not root:
        return
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def bfs(root, target):
    if not root:
        return False
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.value == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False


def get_min(root):
    if not root:
        return sys.maxsize

    left = get_min(root.left)
    right = get_min(root.right)

    return min(root.value, left, right)


def get_sum(root):
    if root is None:
        return 0

    left = get_sum(root=root.left)
    right = get_sum(root.right)

    return left + right + root.value


def get_height(root):
    if root is None:
        return -1

    left = get_height(root=root.left)
    right = get_height(root.right)

    return max(left, right) + 1


def max_path_sum(root):
    if root is None:
        return 0

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)

    return max(left, right) + root.value


def are_symmetric(root1, root2):
    if root1 == root2 is None:
        return True
    if (root1 and not root2) or (root2 and not root1):
        return False
    if root1.value != root2.value:
        return False

    return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)


"""
         50
       /    \ 
      30     70 
     /  \    / \ 
    20  40  60  80
"""
r = None
r = insert(r, 50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("Tree traversal:")
inorder(r)

print("Tree traversal DFS:")
print(dfs(r))
print(dfs_stack(r))
print(bfs_queue(r))
print("Search for 80: {}".format(bfs(r, 80)))
print("Min Value: {}".format(get_min(r)))
print("Max Path Sum: {}".format(max_path_sum(r)))

print("Sum: {}".format(get_sum(r)))
print("Height: {}".format(get_height(r)))
print("IsSymmetric: {}".format(are_symmetric(r.left, r.right)))

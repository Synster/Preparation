"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

    def __repr__(self):
        return self.val


class Solution:
    result = float('-inf')

    def _find_max_path(self, root):
        if not root:
            return 0
        l = self._find_max_path(root.left)
        r = self._find_max_path(root.right)

        max_single = max(max(l, r) + root.val, root.val)  # either take the node or node + maximum child

        max_top = max(l + r + root.val, max_single)  # either take full tree or max_single

        self.result = max(self.result, max_top)

        return max_single

    def maxPathSum(self, root: TreeNode) -> int:
        self._find_max_path(root)
        return self.result


if __name__ == "__main__":
    rtree = TreeNode(20)
    rtree.left = TreeNode(15)
    rtree.right = TreeNode(7)
    tree = TreeNode(-10)
    tree.left = TreeNode(9)
    tree.right = rtree
    print(Solution().maxPathSum(tree))

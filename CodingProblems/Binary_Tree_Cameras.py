# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, parent):
        if root == None:
            return

        self.dfs(root.left, root)
        self.dfs(root.right, root)

        if (parent == None and self.covered.get(root) == None) or self.covered.get(root.left) == None or self.covered.get(root.right) == None:
            self.ans += 1
            self.covered[parent] = True
            self.covered[root] = True
            self.covered[root.left] = True
            self.covered[root.right] = True

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.covered = {}

        self.covered[None] = True

        self.dfs(root, None)

        return self.ans

# Definition for a binary tree node.
from curses.ascii import FS
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    inorder = []

    def inorderTraversal(self, root):
        if root == None:
            return

        self.inorderTraversal(root.left)

        self.inorder.append(root.val)

        self.inorderTraversal(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.inorder.clear()

        self.inorderTraversal(root)

        n = len(self.inorder)
        l = 0
        r = n - 1

        while l < r:
            currentSum = self.inorder[l] + self.inorder[r]
            if currentSum == k:
                return True
            elif currentSum > k:
                r -= 1
            else:
                l += 1

        return False

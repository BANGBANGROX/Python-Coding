# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return root

        if val > root.val:
            return self.search(root.right, val)

        if val == root.val:
            return root

        if val < root.val:
            return self.search(root.left, val)

        return root

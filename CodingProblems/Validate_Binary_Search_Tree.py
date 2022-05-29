# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    inf = int(1e10 + 5)

    def isValidBST(self, root: Optional[TreeNode], maxVal=inf, minVal=-1 * inf) -> bool:
        if root == None:
            return True

        if root.val >= maxVal or root.val <= minVal:
            return False

        return self.isValidBST(root.left, root.val, minVal) & self.isValidBST(root.right, maxVal, root.val)

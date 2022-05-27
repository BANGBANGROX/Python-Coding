# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, pathSum=0) -> bool:
        if root == None:
            return False

        if root.left == None and root.right == None:
            return pathSum + root.val == targetSum

        return self.hasPathSum(root.left, targetSum, pathSum + root.val) | self.hasPathSum(root.right, targetSum, pathSum + root.val)

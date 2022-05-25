from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1 = []
        s2 = []
        ans = []

        s1.append(root)

        while s1:
            current = s1.pop()
            s2.append(current)
            if current.left != None:
                s1.append(current.left)
            if current.right != None:
                s1.append(current.right)

        while s2:
            ans.append(s2.pop())

        return ans

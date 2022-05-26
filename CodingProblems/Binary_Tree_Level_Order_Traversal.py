from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        ans = []

        q.append(root)

        while len(q) > 0:
            n = len(q)
            current = []
            for i in range(n):
                node = q.popleft()
                current.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            ans.append(current)

        return ans

from tkinter.messagebox import NO
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []

        st.append(root)

        while st != []:
            current = st.pop()
            if current == None:
                continue
            ans.append(current.val)
            st.append(current.right)
            st.append(current.left)

        return ans

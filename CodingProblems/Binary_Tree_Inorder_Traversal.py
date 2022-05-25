from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []
        current = root

        while True:
            if current != None:
                st.append(current)
                current = current.left
            elif st:
                current = st.pop()
                ans.append(current.val)
                current = current.right
            else:
                break

        return ans

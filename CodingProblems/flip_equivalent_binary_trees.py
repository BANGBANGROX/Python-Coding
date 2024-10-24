class TreeNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if root1 is None or root2 is None:
            return root1 == root2

        return root1.val == root2.val and (
            (
                self.flipEquiv(root1=root1.left, root2=root2.left)
                and self.flipEquiv(root1=root1.right, root2=root2.right)
            )
            or (
                self.flipEquiv(root1=root1.left, root2=root2.right)
                and self.flipEquiv(root1=root1.right, root2=root2.left)
            )
        )


if __name__ == "__main__":
    root1: TreeNode = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2: TreeNode = TreeNode(4)
    root2.left = TreeNode(5)
    root2.right = TreeNode(6)

    print(Solution().flipEquiv(root1=root1, root2=root2))

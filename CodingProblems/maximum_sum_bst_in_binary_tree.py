class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def __init__(self) -> None:
        self.__answer = 0

    def __dfs(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return [10**9, -(10**9), 0]

        left = self.__dfs(root=root.left)
        right = self.__dfs(root=root.right)

        if left is None or right is None or root.val <= left[1] or root.val >= right[0]:
            return None

        curr_sum = root.val + left[2] + right[2]
        self.__answer = max(self.__answer, curr_sum)

        return [min(root.val, left[0]), max(root.val, right[1]), curr_sum]

    def maxSumBST(self, root: TreeNode) -> int:
        self.__dfs(root=root)

        return self.__answer


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().maxSumBST(root=root))

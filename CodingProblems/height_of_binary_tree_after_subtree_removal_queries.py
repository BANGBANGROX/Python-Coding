class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__max_height_after_removal: dict[int, int] = None
        self.__current_max_height: int = 0

    def __left_to_right_traversal(
        self, root: TreeNode | None, current_height: int
    ) -> None:
        if root is None:
            return

        self.__max_height_after_removal[root.val] = self.__current_max_height
        self.__current_max_height = max(self.__current_max_height, current_height)

        self.__left_to_right_traversal(
            root=root.left, current_height=current_height + 1
        )
        self.__left_to_right_traversal(
            root=root.right, current_height=current_height + 1
        )

    def __right_to_left_traversal(
        self, root: TreeNode | None, current_height: int
    ) -> None:
        if root is None:
            return

        self.__max_height_after_removal[root.val] = max(
            self.__max_height_after_removal[root.val], self.__current_max_height
        )
        self.__current_max_height = max(self.__current_max_height, current_height)

        self.__right_to_left_traversal(
            root=root.right, current_height=current_height + 1
        )
        self.__right_to_left_traversal(
            root=root.left, current_height=current_height + 1
        )

    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        self.__max_height_after_removal = {}
        self.__current_max_height = 0
        answer: list[int] = []

        self.__left_to_right_traversal(root=root, current_height=0)

        self.__current_max_height = 0

        self.__right_to_left_traversal(root=root, current_height=0)

        for query in queries:
            answer.append(self.__max_height_after_removal[query])

        return answer


if __name__ == "__main__":
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    queries: list[int] = [2, 3]

    print(Solution().treeQueries(root=root, queries=queries))

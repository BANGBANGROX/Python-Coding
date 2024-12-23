from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def __get_min_swaps_to_sort(self, nums: list[int]) -> int:
        result: int = 0
        n: int = len(nums)
        sorted_nums: list[int] = sorted(nums)
        nums_index_map: dict[int, int] = {}

        print(nums)
        print(sorted_nums)

        for i in range(n):
            nums_index_map[nums[i]] = i

        for i in range(n):
            if nums[i] != sorted_nums[i]:
                result += 1
                new_index = nums_index_map[sorted_nums[i]]
                nums_index_map[nums[i]] = new_index
                nums[new_index] = nums[i]

        return result

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q: deque[TreeNode] = deque()
        answer: int = 0

        q.append(root)

        while len(q) > 0:
            total: int = len(q)
            nums: list[int] = []
            for _ in range(total):
                node: TreeNode = q.popleft()
                nums.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            answer += self.__get_min_swaps_to_sort(nums)

        return answer


if __name__ == "__main__":
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().minimumOperations(root))
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        queue: list[TreeNode] = []
        pq: list[int] = []

        queue.append(root)

        while len(queue) > 0:
            next_queue: list[TreeNode] = []
            total_sum: int = 0
            for node in queue:
                total_sum += node.val
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
            if len(pq) == k:
                top_val: int = heapq.heappop(pq)
                if total_sum > top_val:
                    heapq.heappush(pq, total_sum)
                else:
                    heapq.heappush(pq, top_val)
            else:
                heapq.heappush(pq, total_sum)
            queue = next_queue

        return heapq.heappop(pq) if len(pq) == k else -1

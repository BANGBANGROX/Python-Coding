from typing import List


class Solution:
    def __init__(self):
        self.dp = None
        self.nums = None

    def _max_coins_handler(self, left: int, right: int) -> int:
        if left > right:
            return 0

        if self.dp[left][right] != -1:
            return self.dp[left][right]

        for mid in range(left, right + 1):
            self.dp[left][right] = max(self.dp[left][right], self._max_coins_handler(left, mid - 1) + self._max_coins_handler(mid + 1, right) + self.nums[left - 1] * self.nums[mid] * self.nums[right + 1])

        return self.dp[left][right]

    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)

        n = len(nums)
        self.nums = nums
        self.dp = [[-1 for _ in range(n)] for __ in range(n)]

        return self._max_coins_handler(1, n - 2)

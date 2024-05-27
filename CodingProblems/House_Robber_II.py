from typing import List


class Solution:
    def _rob_handler(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        return max(self._rob_handler(nums[1:]), self._rob_handler(nums[0:-1]))

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        n = len(nums)

        dp[nums[0] % 3] += nums[0]

        for i in range(1, n):
            nextState = dp
            num = nums[i]
            x = dp[0] + num
            y = dp[1] + num
            z = dp[2] + num
            nextState[x % 3] = max(x, nextState[x % 3])
            nextState[y % 3] = max(y, nextState[y % 3])
            nextState[z % 3] = max(z, nextState[z % 3])
            dp = nextState

        return dp[0]

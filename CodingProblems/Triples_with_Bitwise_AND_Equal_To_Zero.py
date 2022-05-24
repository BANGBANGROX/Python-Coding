from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(n):
                if dp.get(nums[i] & nums[j]) == None:
                    dp[nums[i] & nums[j]] = 0
                dp[nums[i] & nums[j]] += 1

        for i in range(0, n):
            for j in dp:
                if (nums[i] & j) == 0:
                    ans += dp[j]

        return ans

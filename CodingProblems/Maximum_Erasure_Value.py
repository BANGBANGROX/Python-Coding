from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        l = 0
        ans = 0
        totalSum = 0

        for r in range(n):
            if count.get(nums[r]) == None:
                count[nums[r]] = 0
            count[nums[r]] += 1
            totalSum += nums[r]
            while count[nums[r]] > 1:
                count[nums[l]] -= 1
                totalSum -= nums[l]
                l += 1
            ans = max(ans, totalSum)

        return ans

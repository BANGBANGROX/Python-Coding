from typing import List


class Solution:
    def upperBound(self, nums: List[int], key: int):
        n = len(nums)
        l = 0
        r = n - 1
        ans = n

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] > key:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            upper1 = self.upperBound(days, days[i])
            upper2 = self.upperBound(days, days[i] + 6)
            upper3 = self.upperBound(days, days[i] + 29)
            dp[i] += min(dp[upper1] + costs[0], dp[upper2] +
                         costs[1], dp[upper3] + costs[2])

        return dp[0]

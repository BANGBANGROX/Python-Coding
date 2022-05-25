from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        ans = 1

        for i in range(n):
            if dp.get(arr[i] - difference) != None:
                dp[arr[i]] = 1 + dp[arr[i] - difference]
            if dp.get(arr[i]) == None:
                dp[arr[i]] = 1
            ans = max(ans, dp.get(arr[i]))

        return ans

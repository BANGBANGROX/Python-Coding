from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        answer = 1e9
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            current_and = nums[i]
            for j in range(i, n):
                current_and &= nums[j]
                answer = min(answer, abs(k - current_and))
                if current_and <= k or current_and <= dp[j]:
                    break
                dp[j] = current_and

        return answer

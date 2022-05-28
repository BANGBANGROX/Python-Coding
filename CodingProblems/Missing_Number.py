from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = n * (n + 1) // 2
        currentSum = sum(nums)

        return totalSum - currentSum

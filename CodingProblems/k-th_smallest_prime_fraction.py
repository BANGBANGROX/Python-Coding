from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 1
        n = len(nums)

        while left <= right:
            mid = (left + right) / 2
            total_fractions_less_than = 0
            max_fraction = 0
            numerator = -1
            denominator = -1
            j = 1
            for i in range(n):
                while j < n and nums[i] >= nums[j] * mid:
                    j += 1
                total_fractions_less_than += (n - j)
                if j < n and max_fraction < nums[i] / nums[j]:
                    max_fraction = nums[i] / nums[j]
                    numerator = i
                    denominator = j
            if total_fractions_less_than == k:
                return [nums[numerator], nums[denominator]]
            if total_fractions_less_than > k:
                right = mid
            else:
                left = mid

        return [-1, -1]

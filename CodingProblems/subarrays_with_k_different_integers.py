from typing import List

class Solution:
    def _count_subarrays_with_atmost_k(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        left = 0
        count = {}
        distinct_nums = 0

        for right in range(n):
            count[nums[right]] = count.get(nums[right], 0) + 1
            if count[nums[right]] == 1:
                distinct_nums += 1
            while distinct_nums > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    distinct_nums -= 1
                left += 1
            result += (left + 1)

        return result
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._count_subarrays_with_atmost_k(nums, k - 1) - self._count_subarrays_with_atmost_k(nums, k)

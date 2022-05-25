from typing import List


class Solution:
    def lowerBound(self, nums: List[int], key: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        ans = n

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] >= key:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1

        return ans

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda a: (a[0], -a[1]))
        result = []

        for envelope in envelopes:
            pos = self.lowerBound(result, envelope[1])
            if pos == len(result):
                result.append(envelope[1])
            else:
                result[pos] = envelope[1]

        return len(result)

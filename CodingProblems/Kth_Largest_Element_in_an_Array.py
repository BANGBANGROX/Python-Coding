import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        ans = 0

        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            else:
                x = heapq.heappop(pq)
                if num > x:
                    heapq.heappush(pq, num)
                else:
                    heapq.heappush(pq, x)

        while len(pq) > 0:
            ans = heapq.heappop(pq)

        return ans

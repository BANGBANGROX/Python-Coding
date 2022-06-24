from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        pq = []
        currentSum = 0

        for x in target:
            currentSum += x
            heapq.heappush(pq, -1 * x)

        while pq[0] != -1:
            currentSum += pq[0]
            if currentSum == 0 or currentSum >= -1 * pq[0]:
                return False
            old = (-1 * pq[0]) % currentSum
            if currentSum != 1 and old == 0:
                return False
            heapq.heappop(pq)
            heapq.heappush(pq, -1*old)
            currentSum += old

        return True

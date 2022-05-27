from typing import List


class Solution:
    def minJumps(self, n: int, jumps: List[int], last: int) -> int:
        currentMax = 0
        nextMax = 0
        totalJumps = 0

        for i in range(n - 1):
            if i > currentMax:
                return -1
            nextMax = max(nextMax, i + jumps[i])
            if i == currentMax:
                currentMax = nextMax
                totalJumps += 1

        if currentMax >= last:
            return totalJumps

        return -1

    def minTaps(self, n: int, ranges: List[int]) -> int:
        jumps = [0] * (n + 1)

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            jumps[left] = max(jumps[left], right - left)

        return self.minJumps(n + 1, jumps, n)

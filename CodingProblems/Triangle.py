from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        current = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                minValue = current[j]
                if j + 1 < len(current):
                    minValue = min(minValue, current[j + 1])
                triangle[i][j] += minValue
            current = triangle[i]

        return current[0]

from typing import List


class Solution:
    def __init__(self):
        self.dp = None
        self.cuts = None

    def _min_cost_handler(self, left: int, right: int) -> int:
        if left > right:
            return 0

        if self.dp[left][right] != -1:
            return self.dp[left][right]

        self.dp[left][right] = 1e9

        for mid in range(left, right + 1):
            self.dp[left][right] = min(self.dp[left][right], self._min_cost_handler(left, mid - 1) + self._min_cost_handler(mid + 1, right) + self.cuts[right + 1] - self.cuts[left - 1])

        return self.dp[left][right]

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)

        cuts.sort()

        self.cuts = cuts
        self.dp = [[-1 for _ in range(len(cuts))] for __ in range(len(cuts))]

        return self._min_cost_handler(1, len(cuts) - 2)


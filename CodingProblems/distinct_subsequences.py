class Solution:
    def __init__(self):
        self.dp = list(list())
        self.s = None
        self.t = None

    def _num_distinct_handler(self, i: int, j: int) -> int:
        if j >= len(self.t):
            return 1

        if i >= len(self.s):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        self.dp[i][j] = self._num_distinct_handler(i + 1, j) + (
            self._num_distinct_handler(i + 1, j + 1) if self.s[i] == self.t[j] else 0)

        return self.dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        self.s = s
        self.t = t
        self.dp = [[-1 for _ in range(len(t))] for __ in range(len(s))]

        return self._num_distinct_handler(0, 0)
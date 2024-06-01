class Solution:
    def __init__(self):
        self.dp = None
        self.s = None
        self.p = None

    def _is_match_handler(self, i: int, j: int) -> bool:
        if j >= len(self.p):
            return i >= len(self.s)

        if i >= len(self.s):
            return self._is_match_handler(i, j + 1) if self.p[j] == '*' else False

        if self.dp[i][j] != -1:
            return self.dp[i][j] == 1

        if self.s[i] == self.p[j] or self.p[j] == '?':
            self.dp[i][j] = 1 if self._is_match_handler(i + 1, j + 1) else 0
        elif self.p[j] == '*':
            self.dp[i][j] = 1 if self._is_match_handler(i + 1, j) or self._is_match_handler(i + 1, j + 1) or self._is_match_handler(i, j + 1) else 0
        else:
            self.dp[i][j] = 0

        return self.dp[i][j] == 1


    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.dp = [[-1 for _ in range(len(p))] for __ in range(len(s))]

        return self._is_match_handler(0, 0)

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for __ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return n - dp[0][n - 1]

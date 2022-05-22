class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(0, n)]
        ans = n

        for i in range(0, n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = length + i - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    ans += 1

        return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        start = -1
        end = -1
        dp = [[False for _ in range(n)] for __ in range(n)]

        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = length + i - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                elif s[i] == s[j]:
                    dp[i][j] |= dp[i + 1][j - 1]
                if dp[i][j] and length > maxLen:
                    start = i
                    end = j

        return s[start:end+1]
